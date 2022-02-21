"""Users URLs"""

# Django
from django.urls import path

# Local
from nora_menu.users.views import login_view, logout_view,\
    signup_view

urlpatterns = [
    # path('users/', hello_users, name='hello_world'),
    path('users/login/', login_view, name='login'),
    path('users/logout/', logout_view, name='logout'),
    path('users/signup/', signup_view, name='signup'),
]
