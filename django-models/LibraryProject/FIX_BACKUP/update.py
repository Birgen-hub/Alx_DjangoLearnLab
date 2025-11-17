import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from bookshelf.models import Book


b = Book.objects.get(title="1984")
b.title = "Nineteen Eighty-Four"
b.save()
print("Updated:", b.title)
