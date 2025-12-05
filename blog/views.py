from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Post

# Placeholder Views (Assuming previous tasks required these)
def post_new(request):
    return render(request, 'blog/post_form.html', {'title': 'New Post'})
def post_edit(request, pk):
    return render(request, 'blog/post_form.html', {'title': 'Edit Post'})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


# Standard Post List View
def post_list(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'blog/post_list.html', {'posts': posts, 'title': 'All Posts'})

# Search Functionality (Step 3)
def post_search(request):
    query = request.GET.get('q')
    results = []

    if query:
        # Search title, content, or tag name using Q objects
        results = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct().order_by('-id')
    
    return render(request, 'blog/post_search.html', {'query': query, 'results': results})

# View Posts by Tag (Step 5)
def post_by_tag(request, tag_slug):
    posts = Post.objects.filter(tags__slug=tag_slug).order_by('-id')
    tag_name = tag_slug.replace('-', ' ').title()
    context = {
        'posts': posts,
        'title': f'Posts tagged "{tag_name}"',
        'is_tag_view': True
    }
    return render(request, 'blog/post_list.html', context)
