"""Users views"""

# Django
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render


def hello_users(request):
    """List  users"""
    return HttpResponse('Hi Im a user :) ')


def login_view(request):
    """Login view."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(
                request,
                'users/login.html',
                {'error': 'Invalid username and password'}
            )

    return render(request=request, template_name='users/login.html')
