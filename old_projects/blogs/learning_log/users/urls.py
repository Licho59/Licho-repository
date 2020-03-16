'''To define adresses patterns for <users> application.'''
from django.urls import path
from django.contrib.auth.views import login

from . import views

app_name = 'users'
urlpatterns = [
    # Log in website.
    path('login/', login, {'template_name': 'users/login.html'}, name='login'
    ),
    # Log out website.
    path('logout/', views.logout_view, name='logout'),
    
    # Register website.
    path('register/', views.register, name='register'),
]