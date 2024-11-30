from django.db import models

# Create your models here.



class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
Models for the API project.
- Author: Represents an author with a name field.
- Book: Represents a book with title, publication year, and author relationship.
"""

    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
