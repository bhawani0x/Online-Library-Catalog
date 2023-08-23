from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BooksViewSet, AuthorViewSet, MembersViewSet

# Create a router
router = DefaultRouter()
router.register(r'books', BooksViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'members', MembersViewSet)

# Wire up the router's URLs with the views
urlpatterns = [
    # Your other URL patterns
    path('', include(router.urls)),
]
