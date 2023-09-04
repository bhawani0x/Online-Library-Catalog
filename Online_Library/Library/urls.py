# books/urls.py
from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'borrow', BookBorrowingViewSet, basename='book-borrow')


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('book-list', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('author-list', AuthorListView.as_view(), name='author-list'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    path('author/create/', AuthorCreateView.as_view(), name='author-create'),
    path('author/<int:pk>/update/', AuthorUpdateView.as_view(), name='author-update'),
    path('member-list', MemberListView.as_view(), name='member-list'),
    path('member/<int:pk>/', MemberDetailView.as_view(), name='member-detail'),
    path('member/create/', MemberCreateView.as_view(), name='member-create'),
    path('member/<int:pk>/update/', MemberUpdateView.as_view(), name='member-update'),
]+ router.urls