import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from bookshelf.models import Book


try:
    b = Book.objects.get(title="Nineteen Eighty-Four")
    b.delete()
    print("Deleted. Remaining books:", list(Book.objects.all()))
except Book.DoesNotExist:
    print("Book not found for deletion")
