# relationship_app/urls.py
from django.urls import path
from . import views
from .views import list_books, LibraryDetailView, CustomLoginView, CustomLogoutView, register  # Import the views explicitly
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


urlpatterns = [
    # Function-based view for listing books
    path('books/', list_books, name='list_books'),
    
    # Class-based view for displaying details of a specific library
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
      # Login URL
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    
    # Logout URL
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    
    # Registration URL
    path('register/', register, name='register'),
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
]


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
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})



urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]
