from rest_framework import routers
from .views import CallViewSet
from .yasg import schema_view


router = routers.DefaultRouter()
router.register(r'calls', CallViewSet)
