from django.urls import path
from . import views
from .views import PostByTagListView, CommentCreateView, CommentUpdateView, CommentDeleteView

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('search/', views.post_search, name='post_search'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='post_by_tag'),

    # Comment URLs
    path('post/<int:pk>/comments/new/', views.post_detail, name='add_comment'), # Handled by post_detail POST
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='edit_comment'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete_comment'),
]
