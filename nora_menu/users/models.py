"""Users model"""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    """User models.

    Extends from Django's Abstract User in case in the future
    we want to do some changes, also change the username field
    to email and add some extra fields.

    Django recommend do this, because when project is advance
    change the user could be hard.

    src:
    https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#extending-the-existing-user-model
    """

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exist'
        }
    )

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message=(
            'Phone number must be entered in te format: '
            '+999 999 999. Up to 15 digits allowed.'
        )
    )

    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=17,
        blank=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_client = models.BooleanField(
        'client status',
        default=True,
        help_text=(
            'Help easily distinguish users and perform queries. '
            'Clients are the main type of user.'
        )
    )

    def __str__(self) -> str:
        """return username."""
        return self.username

    def get_short_name(self) -> str:
        """Return usermane."""
        return self.username
