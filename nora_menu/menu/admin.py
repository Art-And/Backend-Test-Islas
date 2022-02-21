"""Menu models admin."""

# Django
from django.contrib import admin

# Local
from nora_menu.menu.models import Menu, Option


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """Menu model admin."""

    list_display = (
        'agreed_date',
    )


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    """Option model admin."""

    list_display = (
        'meal',
    )
