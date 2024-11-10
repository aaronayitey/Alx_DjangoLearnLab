from django.shortcuts import render
from .models import Book
from django.views.generic import DetailView
from .models import Library

# Create your views here.

# Function-Based View to list all books
def list_books(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based View to display library details and books
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'