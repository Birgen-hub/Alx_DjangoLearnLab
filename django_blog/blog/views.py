from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Post
from .forms import PostForm # Only importing PostForm now to avoid crash

# Placeholder views
def post_list(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_new(request):
    # This view should handle PostForm submission, currently a placeholder
    return render(request, 'blog/post_form.html', {'title': 'New Post'})

def post_edit(request, pk):
    # This view should handle PostForm submission, currently a placeholder
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

# Posts by Tag Functionality
def post_by_tag(request, tag_slug):
    posts = Post.objects.filter(tags__slug=tag_slug).order_by('-id')
    tag_name = tag_slug.replace('-', ' ').title()
    context = {
        'posts': posts,
        'tag_name': tag_name
    }
    return render(request, 'blog/post_list.html', context)
