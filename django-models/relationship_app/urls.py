# relationship_app/urls.py
from django.urls import path
from .views import list_books, LibraryDetailView  # Import the views explicitly


urlpatterns = [
    # Function-based view for listing books
    path('books/', views.list_books, name='list_books'),
    
    # Class-based view for displaying details of a specific library
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
