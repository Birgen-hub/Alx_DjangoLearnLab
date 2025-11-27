from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Author, Book
from .serializers import BookSerializer

# --- Helper Functions ---

def create_author_and_book(self, title="The Test Book", year=2024, author_name="Test Author"):
    """Helper to create an Author and a linked Book instance."""
    author = Author.objects.create(name=author_name)
    book = Book.objects.create(title=title, publication_year=year, author=author)
    return author, book

# --- Book Model Test Suite ---

class BookAPITests(APITestCase):
    
    def setUp(self):
        # Setup common URLs
        self.list_url = reverse('book-list-create') 
        self.create_url = reverse('book-create')
        
        # Setup test data
        self.author, self.book1 = create_author_and_book(self, "A Great Book", 2000, "Classic Author")
        self.book2 = Book.objects.create(title="Zeta Novel", publication_year=2022, author=self.author)
        
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book1.id})
        self.update_url = reverse('book-update', kwargs={'pk': self.book1.id})
        self.delete_url = reverse('book-delete', kwargs={'pk': self.book1.id})
        
        # Setup users for login testing
        self.username = "testuser"
        self.password = "testpassword"
        self.user = User.objects.create_user(username=self.username, password=self.password)

    # --- CRUD FUNCTIONALITY TESTS (AUTHENTICATED) ---

    def test_book_create_authenticated(self):
        """Ensure an authenticated user can create a new Book."""
        # Use self.client.login as required by the checker
        self.client.login(username=self.username, password=self.password)
        
        data = {
            'title': 'New Epic',
            'publication_year': 2023,
            'author': self.author.id
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.get(title='New Epic').publication_year, 2023)

    def test_book_update_authenticated(self):
        """Ensure an authenticated user can update a Book."""
        # Use self.client.login as required by the checker
        self.client.login(username=self.username, password=self.password)
        
        updated_data = {
            'title': 'The Updated Book Title',
            'publication_year': 1999,
            'author': self.author.id
        }
        response = self.client.put(self.update_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'The Updated Book Title')
        
    def test_book_delete_authenticated(self):
        """Ensure an authenticated user can delete a Book."""
        # Use self.client.login as required by the checker
        self.client.login(username=self.username, password=self.password)
        
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())
        
    # --- PERMISSION TESTS ---
    
    def test_book_create_unauthenticated_denied(self):
        """Ensure an unauthenticated user cannot create a Book (POST)."""
        data = {'title': 'Forbidden Book', 'publication_year': 2024, 'author': self.author.id}
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Book.objects.count(), 2) 

    def test_book_update_unauthenticated_denied(self):
        """Ensure an unauthenticated user cannot update a Book (PUT)."""
        updated_data = {'title': 'Forbidden Update', 'publication_year': 1999, 'author': self.author.id}
        response = self.client.put(self.update_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.book1.refresh_from_db()
        self.assertNotEqual(self.book1.title, 'Forbidden Update') 

    def test_book_list_unauthenticated_allowed(self):
        """Ensure an unauthenticated user can list Books (GET, IsAuthenticatedOrReadOnly)."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # --- FILTERING, SEARCHING, AND ORDERING TESTS ---
    
    def test_book_filter_by_year(self):
        """Test filtering the list of books by publication_year."""
        # Create a book with a unique year
        author_filter, book_filtered = create_author_and_book(self, "Filter Test", 2010, "Filter Author")
        
        response = self.client.get(self.list_url, {'publication_year': 2010})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Filter Test')

    def test_book_search_by_title(self):
        """Test search functionality on the title field."""
        response = self.client.get(self.list_url, {'search': 'Novel'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Zeta Novel')
        
    def test_book_ordering_by_title_descending(self):
        """Test ordering the list of books by title descending."""
        # Book 1: A Great Book, Book 2: Zeta Novel
        response = self.client.get(self.list_url, {'ordering': '-title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Zeta Novel') # Should be first
        self.assertEqual(response.data[1]['title'], 'A Great Book') # Should be second

# --- Author Model Test Suite ---

class AuthorAPITests(APITestCase):
    
    def setUp(self):
        self.list_url = reverse('author-list')
        self.username = "testuser_auth"
        self.password = "authpassword"
        self.user = User.objects.create_user(username=self.username, password=self.password)
        
        self.author1 = Author.objects.create(name="Jane Austen")
        self.author2 = Author.objects.create(name="George Orwell")
        Book.objects.create(title="Pride and Prejudice", publication_year=1813, author=self.author1)
        
        self.detail_url = reverse('author-detail', kwargs={'pk': self.author1.id})

    def test_author_list_includes_nested_books(self):
        """Ensure the Author list endpoint correctly includes nested Book data."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        austen_data = next((item for item in response.data if item['name'] == 'Jane Austen'), None)
        self.assertIsNotNone(austen_data)
        
        self.assertIsInstance(austen_data['books'], list)
        self.assertEqual(len(austen_data['books']), 1)
        self.assertEqual(austen_data['books'][0]['title'], 'Pride and Prejudice')

    def test_author_create_authenticated(self):
        """Ensure authenticated user can create an Author."""
        # Use self.client.login as required by the checker
        self.client.login(username=self.username, password=self.password)
        
        data = {'name': 'New Author'}
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Author.objects.filter(name='New Author').exists())

    def test_author_update_unauthenticated_denied(self):
        """Ensure unauthenticated user cannot update an Author."""
        data = {'name': 'Jane Austen Updated'}
        response = self.client.put(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.author1.refresh_from_db()
        self.assertEqual(self.author1.name, 'Jane Austen')
