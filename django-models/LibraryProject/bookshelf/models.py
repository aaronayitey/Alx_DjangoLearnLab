from typing import Any
from django.db import models

#Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        return f"Book:'{self.title}', Author: {self.author}, Year: {self.publication_year}'"




