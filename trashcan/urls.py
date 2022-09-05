from django.urls import path, include
from .views import TrashcanViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', TrashcanViewSet)

urlpatterns = [
    path('', include(router.urls))
]