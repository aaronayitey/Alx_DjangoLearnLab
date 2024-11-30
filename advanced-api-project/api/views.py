from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.


# List all books
# api/views.py
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated

# ListView for retrieving all books
class ListView(generics.ListAPIView):
    """
    Retrieve a list of all books from the database.
    This view uses the BookSerializer to serialize the data.
    GET /books/
    """
    queryset = Book.objects.all()  # Retrieve all books
    serializer_class = BookSerializer  # Use the BookSerializer for serialization

# DetailView for retrieving a single book by ID
class DetailView(generics.RetrieveAPIView):
    """
    Retrieve a single book by its ID.
    This view uses the BookSerializer to serialize the data.
    GET /books/<int:pk>/
    """
    queryset = Book.objects.all()  # Retrieve books by their primary key (ID)
    serializer_class = BookSerializer  # Use the BookSerializer for serialization

# CreateView for adding a new book
class CreateView(generics.CreateAPIView):
    """
    Create a new book in the database.
    Only authenticated users can create new books.
    POST /books/
    """
    queryset = Book.objects.all()  # Target Book model for creation
    serializer_class = BookSerializer  # Use the BookSerializer to validate and serialize input data
    permission_classes = [IsAuthenticated]  # Only authenticated users can create a book

# UpdateView for modifying an existing book
class UpdateView(generics.UpdateAPIView):
    """
    Update an existing book's details.
    Only authenticated users can update books.
    PUT /books/<int:pk>/
    """
    queryset = Book.objects.all()  # Retrieve books for update by their primary key (ID)
    serializer_class = BookSerializer  # Use the BookSerializer to validate and serialize updated data
    permission_classes = [IsAuthenticated]  # Only authenticated users can update a book

# DeleteView for removing a book
class DeleteView(generics.DestroyAPIView):
    """
    Delete an existing book from the database.
    Only authenticated users can delete books.
    DELETE /books/<int:pk>/
    """
    queryset = Book.objects.all()  # Retrieve books for deletion by their primary key (ID)
    serializer_class = BookSerializer  # Use the BookSerializer to handle any necessary serialization
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete a book

# api/views.py

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Assign the current user as the author
        serializer.save(author=self.request.user)
