from django.urls import path 
from Auth.views import *
urlpatterns = [
    path('', login, name='login'),
]
