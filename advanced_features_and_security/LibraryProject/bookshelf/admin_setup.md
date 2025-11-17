To integrate the Book model with the Django admin interface and customize its display:

1.  **Modify admin.py**:
    The file `bookshelf/admin.py` was updated to import the `Book` model.

2.  **Define Custom Class**:
    A `BookAdmin` class inheriting from `admin.ModelAdmin` was defined to configure the display.
    * list_display: Set to show title, author, and publication_year.
    * list_filter: Configured to allow filtering by publication_year and author.
    * search_fields: Configured to enable searching across title and author.

3.  **Register Model**:
    The model was registered using admin.site.register(Book, BookAdmin).
