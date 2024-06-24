from os import environ
from api.v1 import views
from drf_yasg import openapi
from rest_framework import routers
from django.urls import include, path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('health', csrf_exempt(views.BaseApiView.as_view({'get': 'health'}))),
]

api_url = environ.get('API_URL')
api_port = environ.get('API_PORT')

schema_view = get_schema_view(
    openapi.Info(
        title="OpenVault API",
        default_version='v1',
        description="REST API.",
    ),
    url=f"http://{api_url}:{api_port}",
    public=True,  # False
    permission_classes=(permissions.AllowAny,),
    # permission_classes=(permissions.IsAdminUser,),
)

urlpatterns += [
    #path('swagger/<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view().with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view().with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
