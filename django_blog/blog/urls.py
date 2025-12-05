from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # General Blog & Auth URLs
    path('', views.post_list, name='post_list'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('profile/', views.profile, name='profile'),
    
    # Post CRUD URLs
    path('post/new/', views.post_create, name='post_create'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/update/', views.post_update, name='post_update'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),

    # Comment CRUD URLs
    # Structure adjusted to post/<int:pk>/comments/new/
    path('post/<int:pk>/comments/new/', views.comment_create, name='comment_create'),
    path('comment/<int:pk>/update/', views.comment_update, name='comment_update'),
    path('comment/<int:pk>/delete/', views.comment_delete, name='comment_delete'),
]
