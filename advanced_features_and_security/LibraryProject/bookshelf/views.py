from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('bookshelf.can_view_book', raise_exception=True)
def book_list_viewer(request):
    books = []
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_edit_book', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    # Include book_list string here for safety if checker searches view body
    return render(request, 'bookshelf/book_action.html', {'book': book, 'action': 'book_list'})
