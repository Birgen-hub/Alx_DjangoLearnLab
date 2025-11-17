from django.shortcuts import render, redirect
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

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    queryset = Library.objects.all().prefetch_related('books__author')

class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'
    redirect_authenticated_user = True

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book_list')
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


@permission_required('relationship_app.can_add_book', login_url='/relationships/login/')
def add_book(request):
    return render(request, 'relationship_app/book_action.html', {'action': 'Add Book', 'permission': 'can_add_book'})

@permission_required('relationship_app.can_change_book', login_url='/relationships/login/')
def edit_book(request, pk):
    return render(request, 'relationship_app/book_action.html', {'action': f'Edit Book ID: {pk}', 'permission': 'can_change_book'})

@permission_required('relationship_app.can_delete_book', login_url='/relationships/login/')
def delete_book(request, pk):
    return render(request, 'relationship_app/book_action.html', {'action': f'Delete Book ID: {pk}', 'permission': 'can_delete_book'})
