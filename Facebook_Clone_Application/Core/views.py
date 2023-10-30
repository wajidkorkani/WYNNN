from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
# Create your views here.
def home(request):
    template = 'Core/home.html'
    return render(request, template)

# Current user section
# Creating user profile 
class Create_User_Profile(LoginRequiredMixin, CreateView):
    model = UserProfile
    template_name = 'Core/current-user/Create_User_Profile.html'
    success_url = '/home/'
    fields = ['image', 'city', 'country']
    def form_valid(self, form):
        # Automatically set the user field to the currently logged-in user
        form.instance.user = self.request.user
        form.instance.fname = self.request.user.first_name
        form.instance.lname = self.request.user.last_name
        return super().form_valid(form)
    
# Current user profile page
def current_user_profile(request):
    try:
        profile = get_object_or_404(UserProfile, user=request.user)
        template = 'Core/current-user/current-user-profie-page.html'
        context = {
            'user_profile': profile,
        }
        return render(request, template, context)
    except:
        return redirect('/create-user-profile/')
    