from base64 import b64decode

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.views import View
from .models import ApiToken


class ApiTokenView(View):
    """View for handling issuing and revoking api token."""

    @classmethod
    def authenticate_user(cls, request):
        if 'HTTP_AUTHORIZATION' not in request.META:
            data = {'message': 'Use Basic Auth and supply your username and password.'}
            return JsonResponse(data, status=401)

        auth = request.META['HTTP_AUTHORIZATION'].split()
        if len(auth) != 2 and auth[0].lower() != 'basic':
            data = {'message': 'Use Basic Auth and supply your username and password.'}
            return JsonResponse(data, status=401)

        username, password = b64decode(auth[1]).decode('utf-8').split(':')
        user = authenticate(username=username, password=password)
        if user is None:
            data = {'message': 'Invalid Credentials.'}
            return JsonResponse(data, status=401)

        return user

    def post(self, request, **kwargs):
        if kwargs:
            data = {'message': 'Bad Request.'}
            return JsonResponse(data, status=400)

        response = self.authenticate_user(request)

        if not isinstance(response, User):
            return response

        try:
            api_token, created = ApiToken.objects.get_or_create(owner=response)
        except ValidationError:
            data = {'message': 'Unauthorized.'}
            return JsonResponse(data, status=401)

        data = {'token': api_token.token.hashid}
        return JsonResponse(data, status=201 if created else 200)
