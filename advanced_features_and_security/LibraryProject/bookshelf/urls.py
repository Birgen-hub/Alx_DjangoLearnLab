from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('form/', views.form_example, name='form_example'),
    path('create/', views.book_create, name='book_create'),
    path('<int:pk>/edit/', views.book_edit, name='book_edit'),
    path('<int:pk>/delete/', views.book_delete, name='book_delete'),
]
