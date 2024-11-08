# Utilizing the Django Admin Interface

## Steps Taken:

1. **Registered the Book Model**:
   - In `bookshelf/admin.py`, the `Book` model was registered to make it available in the Django admin interface.

2. **Customized the Admin Interface**:
   - Added a custom `BookAdmin` class to the `bookshelf/admin.py` file.
   - Configured `list_display` to show `title`, `author`, and `publication_year` in the list view.
   - Added filters for `author` and `publication_year` using `list_filter`.
   - Enabled search functionality for `title` and `author` using `search_fields`.

## Outcome:

The Book model is now accessible in the Django admin interface, with enhanced search and filter capabilities for efficient management.
