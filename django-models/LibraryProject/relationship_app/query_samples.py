import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
try:
    django.setup()
except Exception as e:
    print(f'Django setup warning: {e}')

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # Clean up existing data
    Author.objects.all().delete()
    
    # --- 1. Create Sample Data ---
    author1 = Author.objects.create(name='J.K. Rowling')
    author2 = Author.objects.create(name='George Orwell')
    
    book1 = Book.objects.create(title='Harry Potter 1', author=author1)
    book2 = Book.objects.create(title='Harry Potter 2', author=author1)
    book3 = Book.objects.create(title='1984', author=author2)
    
    library_name = 'Central City Library'
    library = Library.objects.create(name=library_name)
    library.books.add(book1, book3)
    
    librarian = Librarian.objects.create(name='Jane Doe', library=library)
    
    print("--- Sample Data Created ---")
    
    # --- 2. Query all books by a specific author (ForeignKey) ---
    print("
--- Query 1: Books by J.K. Rowling (ForeignKey) ---")
    author = Author.objects.get(name='J.K. Rowling')
    books_by_author = Book.objects.filter(author=author)
    for book in books_by_author:
        print(f"- {book.title}")
        
    # --- 3. List all books in a library (ManyToManyField) ---
    print("
--- Query 2: Books in Central City Library (ManyToManyField) ---")
    library_obj = Library.objects.get(name=library_name)
    library_books = library_obj.books.all()
    for book in library_books:
        print(f"- {book.title} (by {book.author.name})")
        
    # --- 4. Retrieve the librarian for a library (OneToOneField) ---
    print("
--- Query 3: Librarian for Central City Library (OneToOneField) ---")
    library_obj = Library.objects.get(name=library_name)
    try:
        lib_staff = library_obj.librarian
        print(f"- Librarian: {lib_staff.name}")
    except Librarian.DoesNotExist:
        print("- No librarian found.")
        
if __name__ == '__main__':
    run_queries()
