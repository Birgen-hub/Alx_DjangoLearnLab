from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm

@permission_required('bookshelf.can_view_book', raise_exception=True)
def book_list(request):
    search_term = request.GET.get('q', '')
    
    if search_term:
        books = Book.objects.filter(title__icontains=search_term).all()
    else:
        books = Book.objects.all()
        
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_edit_book', raise_exception=True)
def form_example(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            return HttpResponse('Form submitted securely and valid')
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})

@permission_required('bookshelf.can_edit_book', raise_exception=True)
def book_edit(request, pk):
    return HttpResponse('Book edit secure')

@permission_required('bookshelf.can_create_book', raise_exception=True)
def book_create(request):
    return HttpResponse('Book create secure')

@permission_required('bookshelf.can_delete_book', raise_exception=True)
def book_delete(request, pk):
    return HttpResponse('Book delete secure')
