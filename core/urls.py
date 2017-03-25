from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from api.auth import authorization_required

urlpatterns = [
    url(r'^', admin.site.urls),
    url(r'^api(/?)$', csrf_exempt(authorization_required(GraphQLView.as_view()))),
    url(r'^api/', include('api.urls')),
    url(r'^graphql/$', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
