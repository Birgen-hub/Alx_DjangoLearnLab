import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from bookshelf.models import Book


books = Book.objects.all()
print("All books:")
for book in books:
    print(book.id, book.title, book.author, book.publication_year)
