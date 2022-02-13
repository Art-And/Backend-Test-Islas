"""Users URLs"""

# Django
from django.urls import path

# Local
from menu.users.views import list_users

urlpatterns = [
    path('users/', list_users)
]
