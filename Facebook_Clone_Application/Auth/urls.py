from django.urls import path 
from Auth.views import *
urlpatterns = [
    path('signup/', Registration, name='signup'),
    path('', login, name='login'),
    path('logout/', user_logout_option, name='logout'),
    path('verify_otp/', verify_otp, name='verify_otp'),
]
