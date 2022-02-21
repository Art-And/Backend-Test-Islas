"""User forms"""

# Django
from django import forms

# Local
from nora_menu.users.models import User


class SignupForm(forms.ModelForm):
    """User signup form"""

    password_confirmation = forms.CharField(
        max_length=128,
        required=True,
    )

    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'password',
            'first_name',
            'last_name',
            'phone_number'
        ]
