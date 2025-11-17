from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from .models import Book, Library
from .forms import CustomUserCreationForm


def list_books(request):
    books = Book.objects.all().select_related('author')
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

@permission_required('relationship_app.can_view_book', login_url='/relationships/login/', raise_exception=True)
def book_list_viewer(request):
    books = Book.objects.all().select_related('author')
    context = {'books': books}
    return render(request, 'relationship_app/book_list_viewer.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    queryset = Library.objects.all().prefetch_related('books__author')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book_list_viewer')
    else:
        form = CustomUserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


def is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and user.userprofile.role == 'Member'

@user_passes_test(is_admin, login_url='/relationships/login/')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian, login_url='/relationships/login/')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member, login_url='/relationships/login/')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


@permission_required('relationship_app.can_create_book', login_url='/relationships/login/', raise_exception=True)
def book_create(request):
    return render(request, 'relationship_app/book_action.html', {'action': 'Create Book', 'permission': 'can_create_book'})

@permission_required('relationship_app.can_edit_book', login_url='/relationships/login/', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'relationship_app/book_action.html', {'action': f'Edit Book ID: {pk}', 'permission': 'can_edit_book', 'book': book})

@permission_required('relationship_app.can_delete_book', login_url='/relationships/login/', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'relationship_app/book_action.html', {'action': f'Delete Book ID: {pk}', 'permission': 'can_delete_book', 'book': book})
