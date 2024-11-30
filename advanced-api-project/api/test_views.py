# api/test_views.py
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Book
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

class BookAPITests(APITestCase):
    """
    Test suite for the Book API endpoints.
    """

    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username="testuser", password="password")
        
        # URL for the Book API
        self.url = reverse('book-list')  # assuming 'book-list' is the name of your BookListView endpoint

        # Create some test books
        self.book1 = Book.objects.create(
            title="Django for Beginners",
            author="John Doe",
            publication_year=2020
        )
        self.book2 = Book.objects.create(
            title="Advanced Django",
            author="Jane Smith",
            publication_year=2021
        )

    def test_create_book(self):
        """
        Test creating a book via the API.
        """
        data = {
            "title": "New Book",
            "author": "Alice",
            "publication_year": 2023
        }
        
        # Authentication required
        self.client.login(username='testuser', password='password')
        
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], data['title'])
        self.assertEqual(response.data['author'], data['author'])
        self.assertEqual(response.data['publication_year'], data['publication_year'])

    def test_update_book(self):
        """
        Test updating a book via the API.
        """
        data = {
            "title": "Updated Book",
            "author": "John Doe",
            "publication_year": 2022
        }
        
        # Authentication required
        self.client.login(username='testuser', password='password')
        
        response = self.client.put(reverse('book-detail', args=[self.book1.id]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], data['title'])
        self.assertEqual(response.data['author'], data['author'])
        self.assertEqual(response.data['publication_year'], data['publication_year'])

    def test_delete_book(self):
        """
        Test deleting a book via the API.
        """
        # Authentication required
        self.client.login(username='testuser', password='password')
        
        response = self.client.delete(reverse('book-detail', args=[self.book1.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())

    def test_filter_books_by_author(self):
        """
        Test filtering books by author.
        """
        response = self.client.get(self.url, {'author': 'John Doe'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], 'John Doe')

    def test_search_books(self):
        """
        Test searching books by title.
        """
        response = self.client.get(self.url, {'search': 'Django'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Both books contain 'Django' in the title

    def test_order_books_by_publication_year(self):
        """
        Test ordering books by publication year.
        """
        response = self.client.get(self.url, {'ordering': 'publication_year'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2020)  # First book should have 2020

    def test_permission_for_create_update_delete(self):
        """
        Test permissions for creating, updating, and deleting books.
        """
        data = {
            "title": "Test Book",
            "author": "Test Author",
            "publication_year": 2022
        }

        # Test non-authenticated user (should fail)
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Authenticate the user
        self.client.login(username='testuser', password='password')

        # Test authenticated user for create (should succeed)
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Test authenticated user for update (should succeed)
        response = self.client.put(reverse('book-detail', args=[self.book1.id]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test authenticated user for delete (should succeed)
        response = self.client.delete(reverse('book-detail', args=[self.book1.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_no_access_for_unauthenticated_user(self):
        """
        Test that an unauthenticated user cannot access any protected endpoints.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
