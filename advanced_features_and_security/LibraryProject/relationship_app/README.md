## Group and Permission-Based Access Control Setup

This application uses custom permissions and Django Groups for granular access control.

### Custom Permissions
Permissions are defined on the `Book` model in `relationship_app/models.py`:
- `can_view_book`
- `can_create_book`
- `can_edit_book`
- `can_delete_book`

### Groups and Assigned Permissions (Admin Setup)
Permissions must be manually assigned to Groups via the Django Admin interface.

| Group | Permissions Assigned |
| :--- | :--- |
| **Admins** | All permissions |
| **Editors** | `can_view_book`, `can_create_book`, `can_edit_book` |
| **Viewers** | `can_view_book` |

### View Enforcement

Access is enforced in `relationship_app/views.py` using the `@permission_required` decorator:

- `book_list_viewer` requires `relationship_app.can_view_book`
- `book_create` requires `relationship_app.can_create_book`
- `book_edit` requires `relationship_app.can_edit_book`
- `book_delete` requires `relationship_app.can_delete_book`

Note: The `raise_exception=True` argument is used to return a 403 Forbidden error if the permission check fails.
