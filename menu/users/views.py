"""Users views"""

# Django
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render


def hello_users(request):
    """List  users"""
    return HttpResponse('Hi Im a user :) ')


def login_view(request):
    """Login view."""

    return render(request=request, template_name='users/login.html')
