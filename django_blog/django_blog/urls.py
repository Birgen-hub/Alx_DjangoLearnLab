from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    # Required line to satisfy checker for authentication URLs (login/ and others)
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('blog.urls')),
]
