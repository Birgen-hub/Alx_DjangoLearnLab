import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
try:
    django.setup()
except Exception as e:
    print(f'Django setup warning: {e}')

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    Author.objects.all().delete()
    
    author_name = 'J.K. Rowling'
    library_name = 'Central City Library'
    
    author1 = Author.objects.create(name=author_name)
    author2 = Author.objects.create(name='George Orwell')
    
    book1 = Book.objects.create(title='Harry Potter 1', author=author1)
    book2 = Book.objects.create(title='Harry Potter 2', author=author1)
    book3 = Book.objects.create(title='1984', author=author2)
    
    library = Library.objects.create(name=library_name)
    library.books.add(book1, book3)
    
    librarian = Librarian.objects.create(name='Jane Doe', library=library)
    
    print("--- Sample Data Created ---")
    
    print("
--- Query 1: Books by J.K. Rowling (ForeignKey) ---")
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)
    for book in books_by_author:
        print(f"- {book.title}")
        
    print("
--- Query 2: Books in Central City Library (ManyToManyField) ---")
    library_obj = Library.objects.get(name=library_name)
    library_books = library_obj.books.all()
    for book in library_books:
        print(f"- {book.title} (by {book.author.name})")
        
    print("
--- Query 3: Librarian for Central City Library (OneToOneField) ---")
    library_obj = Library.objects.get(name=library_name)
    try:
        # Required query: retrieving Librarian by library object
        lib_staff = Librarian.objects.get(library=library_obj)
        print(f"- Librarian: {lib_staff.name}")
    except Librarian.DoesNotExist:
        print("- No librarian found.")
        
if __name__ == '__main__':
    run_queries()
