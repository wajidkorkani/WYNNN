from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
# Create your views here.
def home(request):
    posts = UserPost.objects.all().order_by('-time_stamp')
    template = 'Core/home.html'
    context = {
        'posts': posts,
    }
    return render(request, template, context)

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
    
# Current user posts section 
class Create_User_Post(CreateView):
    model = UserPost
    template_name = 'Core/current-user/Create_Post.html'
    success_url = '/home/'
    fields = ['image', 'video', 'capution']
    def form_valid(self, form):
        # Automatically set the user field to the currently logged-in user
        form.instance.user = self.request.user
        return super().form_valid(form)
    
def post_likes(request, pk):
    url = request.META.get('HTTP_REFERER')
    post = UserPost.objects.filter(id=pk).first()
    if post is not None:
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user.id)
        else:
            post.likes.add(request.user.id)
    return redirect(url)

def current_user_posts(request, slug, pk):
    profile = get_object_or_404(UserProfile, slug=slug, id=pk)
    posts = UserPost.objects.filter(user=profile.user).order_by('-time_stamp')
    template = 'Core/current-user/current_user_posts.html'
    context = {
        'posts': posts
        }
    return render(request, template, context)
