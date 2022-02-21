"""Users views"""

# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

# Local
from nora_menu.users.models import User
from nora_menu.users.forms import SignupForm


def login_view(request):
    """Login view."""

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if not user:
            return render(
                request,
                'users/login.html',
                {'error': 'Invalid username and password'}
            )

        login(request, user)
        return redirect('menu:add_menu')

    return render(request=request, template_name='users/login.html')


def signup_view(request):
    """Signup a User"""

    if request.method == 'POST':

        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            email = data['email']
            username = data['username']
            password = data['password']
            password_confirmation = data['password_confirmation']

            if password != password_confirmation:
                return render(
                    request,
                    'users/signup.html',
                    {
                        'form': {
                            'errors': 'Password confirmation does not match',
                        }
                    }
                )

            user = User.objects.create_user(
                email=email,
                password=password,
                username=username)

            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.phone_number = data['phone_number']
            user.save()

            return redirect('users:login')
    else:
        form = SignupForm()

    return render(
        request=request,
        template_name='users/signup.html',
        context={
            'form': form,
        }
    )


@login_required
def logout_view(request):
    """Logout a user"""

    logout(request)
    return redirect('users:login')
