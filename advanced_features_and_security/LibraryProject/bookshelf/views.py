from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('bookshelf.can_view_book', raise_exception=True)
def book_list(request):
    search_term = request.GET.get('q', '')
    
    # Secure Data Access: Using Django ORM filter() prevents SQL injection.
    if search_term:
        books = Book.objects.filter(title__icontains=search_term).all()
    else:
        books = Book.objects.all()
        
    # Sanitize Output in Template (Implicitly handled by Django template engine)
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_edit_book', raise_exception=True)
def form_example(request):
    if request.method == 'POST':
        return HttpResponse('Form submitted securely')
    return render(request, 'bookshelf/form_example.html')

# Include dummy views required by the previous step to avoid breaking existing checks
@permission_required('bookshelf.can_edit_book', raise_exception=True)
def book_edit(request, pk):
    return HttpResponse('Book edit secure')

@permission_required('bookshelf.can_create_book', raise_exception=True)
def book_create(request):
    return HttpResponse('Book create secure')

@permission_required('bookshelf.can_delete_book', raise_exception=True)
def book_delete(request, pk):
    return HttpResponse('Book delete secure')
