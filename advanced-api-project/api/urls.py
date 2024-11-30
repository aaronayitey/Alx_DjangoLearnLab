# api/urls.py
from django.urls import path
from .views import ListView, DetailView, CreateView, UpdateView, DeleteView

urlpatterns = [
    path('books/', ListView.as_view(), name='book-list'),  # URL for listing all books
    path('books/<int:pk>/', DetailView.as_view(), name='book-detail'),  # URL for retrieving a single book
    path('books/create/', CreateView.as_view(), name='book-create'),  # URL for creating a new book
    path('books/update/<int:pk>/', UpdateView.as_view(), name='book-update'),  # URL for updating a book
    path('books/delete/<int:pk>/', DeleteView.as_view(), name='book-delete'),  # URL for deleting a book
]

