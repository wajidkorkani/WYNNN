from django.contrib import admin
from django.urls import path, include
import Auth
import Core
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Auth.urls')),
    path('', include('Core.urls')),
]
