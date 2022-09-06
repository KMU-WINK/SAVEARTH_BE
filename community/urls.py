from django.urls import path, include
from .views import BoardViewSet, CommentViewSet, LiketViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('board', BoardViewSet, basename='board') # (게시글)
router.register('comment', CommentViewSet, basename='comment') # (댓글)
router.register('like', LiketViewSet, basename='like') # (댓글)

urlpatterns =[
    path('', include(router.urls)),
]