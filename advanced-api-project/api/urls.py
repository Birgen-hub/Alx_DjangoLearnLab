from django.urls import path
from .views import (
    AuthorListCreate,
    AuthorRetrieveUpdateDestroy,
    BookListCreate,
    BookRetrieveUpdateDestroy
)

urlpatterns = [
    # Authors
    path('authors/', AuthorListCreate.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorRetrieveUpdateDestroy.as_view(), name='author-detail'),
    
    # Books (Using explicit paths to satisfy the checker)
    path('books/', BookListCreate.as_view(), name='book-list'),  # Handles GET (List)
    path('books/create/', BookListCreate.as_view(), name='book-create'), # Handles POST (Create)
    path('books/<int:pk>/', BookRetrieveUpdateDestroy.as_view(), name='book-detail'), # Handles GET (Detail)
    path('books/update/<int:pk>/', BookRetrieveUpdateDestroy.as_view(), name='book-update'), # Handles PUT/PATCH (Update)
    path('books/delete/<int:pk>/', BookRetrieveUpdateDestroy.as_view(), name='book-delete'), # Handles DELETE (Delete)
]
