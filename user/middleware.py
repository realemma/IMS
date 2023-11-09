from django.contrib.auth import logout

class SessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            SESSION_COOKIE_AGE = 60 * 10
            # Extend the session timeout if the user is active
            request.session.set_expiry(SESSION_COOKIE_AGE)

        response = self.get_response(request)

        return response