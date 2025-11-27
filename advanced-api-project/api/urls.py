from django.urls import path
from .views import AuthorViewSet, BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('authors', AuthorViewSet)
router.register('books', BookViewSet)

urlpatterns = router.urls
