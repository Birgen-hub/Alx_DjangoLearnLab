from django.contrib import admin
from django.urls import path, include
from knox import views as knox_views
from django.conf.urls.static import static

    path('api/v1/auth/logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    
]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
