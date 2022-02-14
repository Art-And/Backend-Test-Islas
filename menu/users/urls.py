"""Users URLs"""

# Django
from django.urls import path

# Local
from menu.users.views import hello_users, login_view

urlpatterns = [
    path('users/', hello_users, name='hello_world'),
    path('users/login/', login_view, name='login'),
]
