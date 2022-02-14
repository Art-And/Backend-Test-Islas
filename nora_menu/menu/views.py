"""Menu views"""

# Django
from django.shortcuts import redirect, render


def admin_view(request):

    return render(request=request, template_name='base.html')
