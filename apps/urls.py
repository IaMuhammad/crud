from django.urls import path, include
from rest_framework import routers

from apps.views import CategoryModelViewSet, ProductModelViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'categories', CategoryModelViewSet)
router.register(r'products', ProductModelViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
