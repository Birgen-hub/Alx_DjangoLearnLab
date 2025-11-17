import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from bookshelf.models import Book

# CREATE
b = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print("Created:", b)
