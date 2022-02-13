"""User models admin."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Local
from menu.users.models import User


class CustomUserAdmin(UserAdmin):
    """User model admin."""

    list_display = (
        'email',
        'username',
        'first_name',
        'last_name',
        'is_staff',
        'is_client'
    )
    list_filter = ('is_client', 'is_staff')


admin.site.register(User, CustomUserAdmin)
