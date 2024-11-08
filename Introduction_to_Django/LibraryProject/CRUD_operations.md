# Create Operation
>>> from bookshelf.models import Book
>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year
=1949)
>>> book

# Expected Output
<Book: 1984>


# Retrieve Operation

>>> retrieved_book = Book.objects.get(id=book.id)
>>> retrieved_book
<Book: 1984>


# Update Operation

>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> updated_book = Book.objects.get(id=book.id)
>>> updated_book
<Book: Nineteen Eighty-Four>

# Delete Operation

>>> book.delete()
(1, {'bookshelf.Book': 1})
>>> Book.objects.all()
<QuerySet []>