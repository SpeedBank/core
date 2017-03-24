from django.http import JsonResponse

from .models import ApiToken


def authorization_required(func=None):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            """ Don't validate token for a signup query """
            if "createUser" in request.META.get('QUERY_STRING'):
                return view_func(request, *args, **kwargs)

            token_key = 'HTTP_TOKEN'
            if token_key not in request.META:
                data = {'message': 'Set your token in TOKEN header.'}
                return JsonResponse(data, status=401)
            try:
                api_token = ApiToken.objects.get(token=request.META[token_key])
                request.user = api_token.owner
            except (ApiToken.DoesNotExist, TypeError):
                data = {'message': 'Invalid Token.'}
                return JsonResponse(data, status=401)

            return view_func(request, *args, **kwargs)

        return wrapper

    if func:
        return decorator(func)

    return decorator
