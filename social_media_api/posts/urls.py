from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import feed, PostViewSet, CommentViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, basename='post')
router.register('comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', feed),
]
