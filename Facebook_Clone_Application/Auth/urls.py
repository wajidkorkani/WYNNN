from django.urls import path 
from Auth.views import *

urlpatterns = [
    # For signup 
    path('signup/', Registration, name='signup'),
    
    # For login/signin
    path('', login, name='login'),
    
    # For logout/signout
    path('logout/', user_logout_option, name='logout'),
 
    # To verify the email address given by the user to create user account
    path('verify_otp/', verify_otp, name='verify_otp'),
]
