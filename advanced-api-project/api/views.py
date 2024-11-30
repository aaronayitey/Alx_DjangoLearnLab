# api/views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer

# List View for retrieving all books
class ListView(generics.ListAPIView):
    """
    View to list all books.
    - Allows unauthenticated users to view the list of books (read-only access).
    - Authenticated users can access the list as well.
    """
    queryset = Book.objects.all()  # Fetch all Book objects
    serializer_class = BookSerializer  # Use BookSerializer to serialize data
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow read-only access to unauthenticated users

# Detail View for retrieving a single book by ID
class DetailView(generics.RetrieveAPIView):
    """
    View to retrieve a specific book by its ID.
    - Allows unauthenticated users to view details of a single book (read-only access).
    - Authenticated users can access the details as well.
    """
    queryset = Book.objects.all()  # Fetch all Book objects
    serializer_class = BookSerializer  # Use BookSerializer to serialize data
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow read-only access to unauthenticated users

# Create View for adding a new book
class CreateView(generics.CreateAPIView):
    """
    View to create a new book.
    - Only authenticated users can add new books.
    - Authenticated users need to provide valid data to create a book instance.
    """
    queryset = Book.objects.all()  # Fetch all Book objects
    serializer_class = BookSerializer  # Use BookSerializer to serialize data
    permission_classes = [IsAuthenticated]  # Only authenticated users can create books

# Update View for modifying an existing book
class UpdateView(generics.UpdateAPIView):
    """
    View to update an existing book.
    - Only authenticated users can modify the book data.
    - Users must be authenticated to update book details.
    """
    queryset = Book.objects.all()  # Fetch all Book objects
    serializer_class = BookSerializer  # Use BookSerializer to serialize data
    permission_classes = [IsAuthenticated]  # Only authenticated users can update books

# Delete View for removing a book
class DeleteView(generics.DestroyAPIView):
    """
    View to delete a specific book.
    - Only authenticated users can delete a book.
    - Users must be authenticated to delete a book instance.
    """
    queryset = Book.objects.all()  # Fetch all Book objects
    serializer_class = BookSerializer  # Use BookSerializer to serialize data
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete books

# api/views.py

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Assign the current user as the author
        serializer.save(author=self.request.user)

