from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('new/', views.post_new, name='post_new'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('search/', views.post_search, name='post_search'),
    path('tags/<slug:tag_slug>/', views.post_by_tag, name='posts_by_tag'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
]
