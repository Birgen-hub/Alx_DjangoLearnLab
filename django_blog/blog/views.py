from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.views.generic import ListView
from .models import Post
from .forms import PostForm

# Class-based view for filtering posts by tag
class PostByTagListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs.get('tag_slug')).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_slug = self.kwargs.get('tag_slug')
        context['tag_name'] = tag_slug.replace('-', ' ').title()
        return context

# Placeholder function views (kept for existing URLs)
def post_list(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_new(request):
    return render(request, 'blog/post_form.html', {'title': 'New Post'})

def post_edit(request, pk):
    return render(request, 'blog/post_form.html', {'title': 'Edit Post'})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# Search Functionality
def post_search(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct().order_by('-id')
    return render(request, 'blog/post_search.html', {'query': query, 'results': results})
