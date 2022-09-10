from django.urls import path, include
from .views import RouteViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', RouteViewSet)

urlpatterns = [
    path('', include(router.urls))
]