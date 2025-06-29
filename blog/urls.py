from django.urls import path
from .views import (
    home, about,
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,
    PageListView, PageDetailView, PageCreateView, PageUpdateView, PageDeleteView
)

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),

    # Post URLs
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/create/', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

    # Page URLs
    path('pages/', PageListView.as_view(), name='pages-list'),
    path('pages/<int:pk>/', PageDetailView.as_view(), name='page-detail'),
    path('pages/create/', PageCreateView.as_view(), name='page-create'),
    path('pages/<int:pk>/edit/', PageUpdateView.as_view(), name='page-edit'),
    path('pages/<int:pk>/delete/', PageDeleteView.as_view(), name='page-delete'),
]
