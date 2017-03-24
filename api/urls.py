from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from .views import ApiTokenView

urlpatterns = [
    url(r'^login$', csrf_exempt(ApiTokenView.as_view())),
]
