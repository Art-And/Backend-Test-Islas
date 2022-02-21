"""Users views"""

# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.db import IntegrityError

# Local
from nora_menu.users.models import User


def login_view(request):
    """Login view."""

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('menu:add_menu')
        else:
            return render(
                request,
                'users/login.html',
                {'error': 'Invalid username and password'}
            )

    return render(request=request, template_name='users/login.html')


def signup_view(request):
    """Signup a User"""

    if request.method == 'POST':
        email = request.POST['email_username']
        username = request.POST['user_name']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        if password != password_confirmation:
            return render(
                request,
                'users/signup.html',
                {'error': 'Password confirmation does not match'}

            )

        try:
            user = User.objects.create_user(
                email=email,
                password=password,
                username=username)
        except IntegrityError as error:

            return render(
                request,
                'users/signup.html',
                {'error': error}
            )

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.phone_number = request.POST['phone_number']
        user.save()

        return redirect('users:login')

    return render(request=request, template_name='users/signup.html')


@login_required
def logout_view(request):
    """Logout a user"""

    logout(request)
    return redirect('users:login')
