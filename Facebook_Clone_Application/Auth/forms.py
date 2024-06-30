from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# This is Registration Form 
class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')
