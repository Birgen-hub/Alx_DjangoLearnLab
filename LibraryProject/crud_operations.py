import os
import django
from django.db import IntegrityError
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
try:
    django.setup()
except Exception as e:
    print(f'Django setup warning: {e}')
try:
    from bookshelf.models import Book
except ImportError:
    print('FATAL ERROR: Could not import Book model. Check models.py.')
    exit()
def create_book(title: str, author: str, year: int) -> Book | None:
    try:
        book = Book.objects.create(
            title=title,
            author=author,
            publication_year=year
        )
        print(f'CREATED: {book.title} by {book.author}')
        return book
    except Exception as e:
        print(f'CREATE FAILED: {e}')
        return None
def read_all_books():
    print('
--- Reading All Books ---')
    books = Book.objects.all()
    if not books:
        print('No books found.')
        return []
    for book in books:
        print(f'ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.publication_year}')
    return books
def update_book_year(book_id: int, new_year: int) -> Book | None:
    try:
        book = Book.objects.get(id=book_id)
        old_year = book.publication_year
        book.publication_year = new_year
        book.save()
        print(f'
UPDATED: Book ID {book_id} ("{book.title}") year changed from {old_year} to {new_year}')
        return book
    except Book.DoesNotExist:
        print(f'
UPDATE FAILED: Book with ID {book_id} does not exist.')
        return None
def delete_book(book_id: int) -> bool:
    try:
        book = Book.objects.get(id=book_id)
        title = book.title
        book.delete()
        print(f'
DELETED: Book ID {book_id} ("{title}")')
        return True
    except Book.DoesNotExist:
        print(f'
DELETE FAILED: Book with ID {book_id} does not exist.')
        return False
if __name__ == '__main__':
    print('--- Starting CRUD Operations Demonstration ---')
    try:
        Book.objects.all().delete()
    except Exception:
        pass
    book1 = create_book('Dune', 'Frank Herbert', 1965)
    book2 = create_book('1984', 'George Orwell', 1949)
    book3 = create_book('To Kill a Mockingbird', 'Harper Lee', 1960)
    read_all_books()
    if book1:
        update_book_year(book1.id, 1966)
    if book2:
        delete_book(book2.id)
    read_all_books()
    print('
--- CRUD Operations Demonstration Complete ---')
