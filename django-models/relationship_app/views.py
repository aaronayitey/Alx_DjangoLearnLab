from django.shortcuts import render, redirect
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView

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

# Login View (built-in)
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# Logout View (built-in)
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

# Registration View (Custom)
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after registration
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
