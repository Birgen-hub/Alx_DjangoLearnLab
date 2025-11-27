from django.urls import path
from .views import AuthorList, BookList

urlpatterns = [
    path('authors/', AuthorList.as_view(), name='author-list'),
    path('books/', BookList.as_view(), name='book-list'),
]
