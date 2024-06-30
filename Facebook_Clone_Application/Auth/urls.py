from django.urls import path 
from Auth.views import *

urlpatterns = [

    # This url is for signup
    path('signup/', Registration, name='signup'),

    # This url is for login 
    path('', login, name='login'),

    # This url is for logout 
    path('logout/', user_logout_option, name='logout'),

    # This url is for email otp verification 
    path('verify_otp/', verify_otp, name='verify_otp'),
]
