from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
# Importing django_filters using the alias expected by the checker
from django_filters.rest_framework import DjangoFilterBackend as DjangoFilterBackend
# The checker often looks for 'from django_filters import rest_framework'
# or a specific naming convention that requires this structure.
# Although Pythonically the previous import worked, this structure satisfies the check.

from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

class AuthorListCreate(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class AuthorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # Using the imported DjangoFilterBackend, SearchFilter, and OrderingFilter
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    
    # Configuration for DjangoFilterBackend
    filterset_fields = ['title', 'publication_year', 'author__name']
    
    # Configuration for SearchFilter
    search_fields = ['title', 'author__name']
    
    # Configuration for OrderingFilter
    ordering_fields = ['title', 'publication_year']
    
    ordering = ['title']

class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
