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

# api/views.py
from django_filters import rest_framework as filters
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# Book Filter class to filter by title, author, and publication year
class BookFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')  # Case-insensitive search
    author = filters.CharFilter(lookup_expr='icontains')  # Case-insensitive search
    publication_year = filters.NumberFilter()

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

# BookListView now uses filtering
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BookFilter


# api/views.py
from rest_framework import filters

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter)
    filterset_class = BookFilter
    search_fields = ['title', 'author']  # Enable search on title and author


# api/views.py
from rest_framework import filters

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_class = BookFilter
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']  # Allow ordering by title and publication year
    ordering = ['title']  # Default ordering by title


# api/views.py
from django_filters import rest_framework as filters
from rest_framework import generics, filters as drf_filters
from .models import Book
from .serializers import BookSerializer

class BookFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    author = filters.CharFilter(lookup_expr='icontains')
    publication_year = filters.NumberFilter()

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

class BookListView(generics.ListAPIView):
    """
    List all books with filtering, searching, and ordering.
    - Filter by title, author, and publication year.
    - Search by title and author.
    - Order by title or publication year.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (filters.DjangoFilterBackend, drf_filters.SearchFilter, drf_filters.OrderingFilter)
    filterset_class = BookFilter
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering by title
