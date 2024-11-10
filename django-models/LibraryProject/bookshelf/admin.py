from django.contrib import admin
from .models import Book
# Register your models here.


# Register the Book model
# Define a custom admin class for Book model
class BookAdmin(admin.ModelAdmin):
    # Specify the fields to be displayed in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add filters to the right sidebar for quick filtering
    list_filter = ('author', 'publication_year')

    # Enable search functionality
    search_fields = ('title', 'author')

# Register the Book model with the custom BookAdmin configuration
admin.site.register(Book, BookAdmin)