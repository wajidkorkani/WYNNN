from django.urls import path 
from Core.views import *
urlpatterns = [
    path('home/', home, name='home'),
]
