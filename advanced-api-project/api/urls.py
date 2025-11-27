from django.urls import path
from .views import AuthorList, AuthorDetail, BookList, BookDetail

urlpatterns = [
    path('authors/', AuthorList.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorDetail.as_view(), name='author-detail'),
    path('books/', BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
]
