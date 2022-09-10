from django.urls import path, include
from .views import TrashViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', TrashViewSet)

urlpatterns = [
    path('', include(router.urls))
]