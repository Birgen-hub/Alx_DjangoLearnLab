import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from bookshelf.models import Book

# ---------- CREATE ----------
b = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print("Created:", b)

# ---------- RETRIEVE ----------
books = Book.objects.all()
print("All books:")
for book in books:
    print(book.id, book.title, book.author, book.publication_year)

# ---------- UPDATE ----------
b = Book.objects.get(title="1984")
b.title = "Nineteen Eighty-Four"
b.save()
print("Updated:", b.title)

# ---------- DELETE ----------
b.delete()
books = Book.objects.all()
print("Deleted. Remaining books:", list(books))
