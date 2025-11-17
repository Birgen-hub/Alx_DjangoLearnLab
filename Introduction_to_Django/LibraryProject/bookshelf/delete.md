python manage.py shell
book = Book.objects.get(title='Nineteen Eighty-Four')
book.delete()
