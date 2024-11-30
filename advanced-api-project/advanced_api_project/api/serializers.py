from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    """
Serializers for the API project.
- BookSerializer: Serializes all fields of the Book model, with validation for publication year.
- AuthorSerializer: Serializes the Author model, including nested serialization for related books.
"""

    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        import datetime
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
