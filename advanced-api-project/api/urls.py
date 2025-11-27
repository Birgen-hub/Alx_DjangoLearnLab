from django.urls import path
from .views import (
    AuthorListCreate,
    AuthorRetrieveUpdateDestroy,
    BookListCreate,
    BookRetrieveUpdateDestroy
)

urlpatterns = [
    # Authors
    path('authors/', AuthorListCreate.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorRetrieveUpdateDestroy.as_view(), name='author-detail'),
    
    # Books
    path('books/', BookListCreate.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroy.as_view(), name='book-detail'),
]
