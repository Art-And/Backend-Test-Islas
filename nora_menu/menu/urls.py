"""Users URLs"""

# Django
from django.urls import path

# Local
from nora_menu.menu.views import admin_view

urlpatterns = [
    path('menu/', admin_view, name='add_menu'),
]
