"""Users views"""

# Django
from django.http import HttpResponse


def list_users(request):
    """List  users"""
    return HttpResponse('Que onda soy el users :) ')
