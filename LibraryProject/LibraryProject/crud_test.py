import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from bookshelf.models import Book

# ---------- CREATE ----------
b = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print("CREATE:")
print(f"{b.id} {b.title} {b.author} {b.publication_year}\n")

# ---------- RETRIEVE ----------
books = Book.objects.all()
print("RETRIEVE:")
for book in books:
    print(f"{book.id} {book.title} {book.author} {book.publication_year}")
print()

# ---------- UPDATE ----------
b.title = "Nineteen Eighty-Four"
b.save()
print("UPDATE:")
for book in Book.objects.all():
    print(f"{book.id} {book.title} {book.author} {book.publication_year}")
print()

# ---------- DELETE ----------
b.delete()
print("DELETE:")
print("Remaining books:", list(Book.objects.all()))
