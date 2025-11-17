from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from . import views

urlpatterns = [
    path('books/', views.list_books, name='book_list'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html', next_page='login'), name='logout'),
    path('register/', views.register, name='register'),

    path('admin-dashboard/', views.admin_view, name='admin_view'),
    path('librarian-tools/', views.librarian_view, name='librarian_view'),
    path('member-area/', views.member_view, name='member_view'),

    path('books/secure/list/', views.book_list_viewer, name='book_list_viewer'),
    path('books/secure/create/', views.book_create, name='book_create'),
    path('books/secure/<int:pk>/edit/', views.book_edit, name='book_edit'),
    path('books/secure/<int:pk>/delete/', views.book_delete, name='book_delete'),
]
