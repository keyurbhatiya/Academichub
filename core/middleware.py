# core/middleware.py

from datetime import timedelta
from django.utils import timezone
from django.conf import settings

class AdminSessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and request.user.is_staff:
            now = timezone.now()
            last_activity = request.session.get('last_activity')

            if last_activity:
                elapsed = (now - timezone.datetime.fromisoformat(last_activity)).total_seconds()
                if elapsed > 1800:  # 30 minutes
                    from django.contrib.auth import logout
                    logout(request)
            request.session['last_activity'] = now.isoformat()
        return self.get_response(request)
