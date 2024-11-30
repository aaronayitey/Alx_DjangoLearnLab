# API Documentation

## Endpoints:

- **GET /books/**: Retrieve a list of all books (Public).
- **GET /books/{id}/**: Retrieve a single book by ID (Public).
- **POST /books/create/**: Create a new book (Authenticated only).
- **PUT /books/{id}/update/**: Update an existing book (Authenticated only).
- **DELETE /books/{id}/delete/**: Delete a book (Authenticated only).

## Permissions:

- **Create, Update, Delete**: Restricted to authenticated users only.
- **List and Detail**: Accessible by both authenticated and unauthenticated users.
