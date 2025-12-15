from django.urls import path
from .views import NotificationListView, NotificationCreateView, NotificationUpdateView

urlpatterns = [
    path('', NotificationListView.as_view(), name='notifications-list'),
    path('create/', NotificationCreateView.as_view(), name='notifications-create'),
    path('update/<int:pk>/', NotificationUpdateView.as_view(), name='notifications-update'),
]
