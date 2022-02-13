"""Main URLs module.

my site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin

# from .utils.healthz import healthz

urlpatterns = [
    # Django Admin
    path('admin_menu', admin.site.urls),

    path('', include(('menu.users.urls', 'users'), namespace='user')),
    # path("healthz", healthz, name="healthz"),
]

# If you want to show media in dev, please add next line of code to show it.
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
