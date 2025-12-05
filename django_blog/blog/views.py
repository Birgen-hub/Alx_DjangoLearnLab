from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from .forms import UserRegisterForm, ProfileUpdateForm, PostForm, CommentForm
from .models import Post, Comment

# --- Authentication Views ---

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Account created for {user.username}!')
            return redirect('post_list')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'blog/profile.html', {'form': form})


# --- Post CRUD Views ---

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date']
post_list = PostListView.as_view()

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 1. Add comment form for display (submission goes to CommentCreateView)
        context['comment_form'] = CommentForm()
        # 2. Fetch all comments for the post
        context['comments'] = self.object.comments.all()
        return context

# The .post() method for handling comment submission is removed and moved to CommentCreateView
post_detail = PostDetailView.as_view()


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Your post has been created!')
        return super().form_valid(form)
post_create = PostCreateView.as_view()


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        messages.success(self.request, 'Your post has been updated!')
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
post_update = PostUpdateView.as_view()


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list') 

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
    def form_valid(self, form):
        messages.success(self.request, 'Your post has been deleted.')
        return super().form_valid(form)
post_delete = PostDeleteView.as_view()


# --- Comment CRUD Views ---

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    # Note: This view does not render its own template; it is called by POST from post_detail.html

    def form_valid(self, form):
        # Get the Post object using the 'post_pk' passed in the URL
        post = get_object_or_404(Post, pk=self.kwargs['post_pk'])
        
        comment = form.save(commit=False)
        comment.post = post
        comment.author = self.request.user
        comment.save()
        
        messages.success(self.request, 'Your comment has been posted.')
        return super().form_valid(form)

    # After successful creation, redirect back to the post detail page
    def get_success_url(self):
        # Use the post_pk from the URL kwargs to redirect
        return reverse('post_detail', kwargs={'pk': self.kwargs['post_pk']})
comment_create = CommentCreateView.as_view()


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'
    
    def get_success_url(self):
        messages.success(self.request, 'Your comment has been updated.')
        return reverse('post_detail', kwargs={'pk': self.object.post.pk})

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
comment_update = CommentUpdateView.as_view()

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'
    
    def get_success_url(self):
        messages.success(self.request, 'Your comment has been deleted.')
        return reverse('post_detail', kwargs={'pk': self.object.post.pk})

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
comment_delete = CommentDeleteView.as_view()
