"""Global middlewares"""

# Django
from django.conf import settings
from django.contrib.sessions.middleware import SessionMiddleware
from django.utils.cache import add_never_cache_headers
from django.shortcuts import redirect
from django.urls import reverse


class HealthCheckAwareSessionMiddleware(SessionMiddleware):
    def process_request(self, request):
        if request.path_info.startswith("/healthz"):
            request.COOKIES[settings.SESSION_COOKIE_NAME] = "healthcheck"
        super(HealthCheckAwareSessionMiddleware, self).process_request(request)


class HeaderNoCacheMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.method == "GET"\
           and not response.has_header("Cache-Control"):
            add_never_cache_headers(response)

        return response


class RedirectToMenuMiddleware:
    """Redirect to menu middleware

    Every time that user is auth, the next urls list can not be load,
    and will be redirect to user home page.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if not request.user.is_anonymous:
            urls = [reverse('users:login'), reverse('users:signup')]

            if request.path in urls:
                return redirect('menu:add_menu')

        response = self.get_response(request)
        return response
