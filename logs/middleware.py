from django.utils.deprecation import MiddlewareMixin
from .models import APILog

class APILogMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Save request body for later use
        request._body = request.body

    def process_response(self, request, response):
        try:
            user = request.user if request.user.is_authenticated else None
        except Exception:
            user = None

        try:
            request_payload = request._body.decode('utf-8') if hasattr(request, '_body') else ''
        except Exception:
            request_payload = ''

        try:
            response_payload = response.content.decode('utf-8')
        except Exception:
            response_payload = ''

        # Log the API call
        APILog.objects.create(
            user=user,
            method=request.method,
            endpoint=request.path,
            request_payload=request_payload,
            response_payload=response_payload,
            status_code=response.status_code
        )
        return response
