python manage.py shell
book = Book.objects.get(title='1984')
book.publication_year = 2000
book.save()
