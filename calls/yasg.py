from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title='Get external Farm saved API',
        default_version='v1',
        description='Yeah just kind of a test app',
        license=openapi.License(name='THC Licence'),

    ),
    public=True,
)

urlpatterns = [
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-calls')
]
