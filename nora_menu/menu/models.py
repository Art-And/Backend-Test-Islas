"""Menu models"""

# Django
from django.db import models


class Option(models.Model):
    """Option model."""

    meal = models.CharField(
        'meal name',
        max_length=255,
        help_text=('meal option')
    )


class Menu(models.Model):
    """Menu model.

    Specific meals create a complete menu.
    """

    title_text = models.TextField(
        blank=True,
        null=True,
        help_text=(
            'greeting or menu description'
        )
    )

    option_meals = models.ManyToManyField(
        to='option',
        related_name='meals',
    )

    agreed_date = models.DateField(null=True, blank=True, default=None)

    create_date = models.DateTimeField(auto_now_add=True)

    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        """return username."""
        return self.agreed_date

    def get_short_name(self) -> str:
        """Return usermane."""
        return self.agreed_date
