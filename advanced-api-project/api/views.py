from rest_framework import generics
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

class AuthorList(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
