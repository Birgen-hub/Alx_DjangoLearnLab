from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

# Maps to List and Create (equivalent to ListView and CreateView functionality)
class AuthorListCreate(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    # Applying permissions
    permission_classes = [IsAuthenticatedOrReadOnly]

# Maps to Retrieve, Update, and Destroy (equivalent to DetailView, UpdateView, DeleteView functionality)
class AuthorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    # Applying permissions
    permission_classes = [IsAuthenticatedOrReadOnly]

# Maps to List and Create
class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Applying permissions
    permission_classes = [IsAuthenticatedOrReadOnly]

# Maps to Retrieve, Update, and Destroy
class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Applying permissions
    permission_classes = [IsAuthenticatedOrReadOnly]
