from django.urls import path 
from Core.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('home/', home, name='home'),
    path('create-user-profile/', Create_User_Profile.as_view(), name='Create_User_Profile'),
    path('me/', current_user_profile, name='current_user_profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
