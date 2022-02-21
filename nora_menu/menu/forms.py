"""Menu forms"""

# Django
from django import forms

# Local
from nora_menu.menu.models import Menu


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'
