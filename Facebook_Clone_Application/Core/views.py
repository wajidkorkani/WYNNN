from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import CommentForm, ReplyForm, AIChatForm, PostCommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# This view is for landing page or home page 
@login_required
def home(request):
    try:
        profile = get_object_or_404(UserProfile, user=request.user)
        posts = UserPost.objects.all().order_by('-time_stamp')
        template = 'Core/home.html'
        context = {
            'posts': posts,
            'profile': profile,
        }
        return render(request, template, context)
    except:
        return redirect('/create-user-profile/')



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

# To Change the profile image 
class Change_User_Profile_Image(LoginRequiredMixin, UpdateView):
    model = UserProfile
    template_name = 'Core/current-user/Change_User_Profile_Image.html'
    success_url = '/home/'
    fields = ['image']
    def form_valid(self, form):
        # Automatically set the user field to the currently logged-in user
        form.instance.user = self.request.user
        return super().form_valid(form)

# This view is for delete own profile
class Delete_Profile(DeleteView):
    model = UserProfile
    fields = '__all__'
    template_name = 'Core/current-user/delete_profile.html'
    success_url = '/home/'

# This view is for update profile
class Update_Profile(UpdateView):
    model = UserProfile
    fields = ['email', 'fname', 'lname', 'city', 'country']
    template_name = 'Core/current-user/updateProfile.html'
    success_url = '/me/'

# Current user profile page
@login_required
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
    template_name = 'Core/current-user/create_post.html'
    success_url = '/me/'
    fields = ['image', 'capution']
    def form_valid(self, form):
        # Automatically set the user field to the currently logged-in user
        profileID = self.kwargs.get('pk')
        form.instance.profile = get_object_or_404(UserProfile, id=profileID)
        return super().form_valid(form)


# This view is for to like any post uploaded by any user
@login_required
def post_likes(request, pk):
    profile = get_object_or_404(UserProfile, user=request.user)
    url = request.META.get('HTTP_REFERER')
    post = UserPost.objects.filter(id=pk).first()
    if post is not None:
        if post.likes.filter(id=profile.id).exists():
            post.likes.remove(profile.id)
        else:
            post.likes.add(profile.id)
    return redirect(url)


# This view is for current user posts
@login_required
def current_user_posts(request, slug, pk):
    profile = get_object_or_404(UserProfile, slug=slug, id=pk)
    posts = UserPost.objects.filter(profile=profile).order_by('-time_stamp')
    template = 'Core/current-user/current_user_posts.html'
    context = {
        'posts': posts,
        'profile':profile
        }
    return render(request, template, context)

# This method is for submiting comment on post.
@login_required
def postComment(request, pk):
    url = request.META.get('HTTP_REFERER')
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = PostCommentForm(request.POST)
        if form.is_valid():
            data = PostComment()
            data.comment = form.cleaned_data['comment']
            data.ip = request.META.get('REMOTE_ADDR')
            data.post_id = pk
            data.profile_id = profile.id
            data.save()
            return redirect(url)

def postCommentsPage(request, pk):
    post = get_object_or_404(UserPost, id=pk)
    comments = PostComment.objects.filter(post=post)
    template = 'Core/all-users/postCommentsPage.html'
    context = {
        "post":post,
        "comments":comments
    }
    return render(request, template, context)

# This view is for to delete own posts
class Delete_Post(DeleteView):
    model = UserPost
    fields = '__all__'
    template_name = 'Core/current-user/delete_post.html'
    success_url = '/home/'




# Blog Section Starts from here

# All blog views are here
class Create_Blog(CreateView):
    model = Blog
    template_name = 'Core/current-user/Create_Blog.html'
    success_url = '/home/'
    fields = ['image', 'title', 'category','text']
    def form_valid(self, form):
        # Automatically set the user field to the currently logged-in user
        profileID = self.kwargs.get('pk')
        form.instance.profile = get_object_or_404(UserProfile, id=profileID)
        return super().form_valid(form)


# This view is for all blogs
@login_required
def all_blogs(request):
    blogs = Blog.objects.all().order_by('-time_stamp')
    template = 'Core/current-user/all_blogs.html'
    context = {
        'blogs': blogs
    }
    return render(request, template, context)


# This view is for about page of the blogs
@login_required
def blog_about_page(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    profile = Blog.objects.get(id=pk)
    comment = BlogComment.objects.filter(blog__id=profile.id)
    template = 'Core/current-user/blog_about_page.html'
    context = {
        'blog': blog,
        'comments': comment
        }
    return render(request, template, context)


# This view is where all replies will be displayed with the comment in on which users replied 
@login_required
def blog_comment_about_page(request, pk):
    comment = get_object_or_404(BlogComment, id=pk)
    replies = BlogCommentReply.objects.filter(blog_comment__id=comment.id)
    template = 'Core/current-user/blog_comment_reply.html'
    context = {
        'comment': comment,
        'replies': replies
    }
    return render(request, template, context)


# This view is for to add review or comment on the blogs
@login_required
def submit_blog_review(request, blog_id):
    url = request.META.get('HTTP_REFERER')
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = BlogComment()
            data.comment = form.cleaned_data['comment']
            data.ip = request.META.get('REMOTE_ADDR')
            data.blog_id = blog_id
            data.profile_id = profile.id
            data.save()
            return redirect(url)


# This view is for to reply on comments
@login_required
def submit_comment_reply(request, comment_id):
    url = request.META.get('HTTP_REFERER')
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            data = BlogCommentReply()
            data.reply = form.cleaned_data['reply']
            data.ip = request.META.get('REMOTE_ADDR')
            data.blog_comment_id = comment_id
            data.profile_id = profile.id
            data.save()
            return redirect(url)


# This view is where all blogs will be displayed uploaded by the current user
@login_required
def current_user_blogs(request, slug, pk):
    profile = get_object_or_404(UserProfile, slug=slug, id=pk)
    blog = Blog.objects.filter(profile=profile).order_by('-time_stamp')
    template = 'Core/current-user/current_user_blogs.html'
    context = {
        'blogs':blog,
        'profile':profile
        }
    return render(request, template, context)

# This view is to delete own blogs
class Delete_Blog(DeleteView):
    model = Blog
    fields = '__all__'
    template_name = 'Core/current-user/blogs_delete.html'
    success_url = '/home/'


# This is searchbar section

@login_required
def searchbar(request):
    searched = request.POST["searched"]
    users = UserProfile.objects.filter(lname__contains=searched)
    user_fname = UserProfile.objects.filter(fname__contains=searched)
    posts = UserPost.objects.filter(capution__contains=searched)
    blog = Blog.objects.filter(title__iexact=searched)
    blogs = Blog.objects.filter(title__icontains=searched)
    blogs_category = Blog.objects.filter(category__icontains=searched)
    template = 'Core/searchbar.html'
    context = {
        'users':users,
        'user_fname':user_fname,
        'posts':posts,
        'blog':blog,
        'blogs':blogs,
        'blogs_category': blogs_category}
    return render(request, template, context)



# Section all users starts from here

# This view is where all users profiles will be display
@login_required
def all_users_profile_page(request, pk):
    profile = UserProfile.objects.get(id=pk)
    template = 'Core/all-users/all_users_profile_page.html'
    context = {
        'users' : profile
    }
    return render(request, template, context)


# This view is where all users posts will be display
@login_required
def all_users_posts(request, slug, pk):
    profile = get_object_or_404(UserProfile, slug=slug, id=pk)
    posts = UserPost.objects.filter(profile=profile).order_by('-time_stamp')
    template = 'Core/all-users/all_users_posts.html'
    context = {
        'posts': posts,
        'profile':profile
    }
    return render(request, template, context)


# This view is where all users blogs will be display
@login_required
def all_users_blogs(request, slug, pk):
    profile = get_object_or_404(UserProfile, slug=slug, id=pk)
    blog = Blog.objects.filter(profile=profile).order_by('-time_stamp')
    template = 'Core/all-users/all_users_blogs.html'
    context = {
        'blogs':blog,
        'profile':profile
    }
    return render(request, template, context)


# This is message section
@login_required
def AIChat(request):
    try:
        profile = get_object_or_404(UserProfile, user=request.user)
        chatData = Chat.objects.filter(user=profile).order_by('-id')
        template = "aiChat.html"
        context = {
            'chatData' : chatData
        }
        return render(request, template, context)
    except:
        return redirect('/create-user-profile/')

import google.generativeai as genai
API_KEY = ""
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# This is method will send question and receive answer
def chatWithAI(request):
    if request.method == 'POST':
        url = request.META.get('HTTP_REFERER')
        question = request.POST.get('ask')
        answer = model.generate_content([question])
        profile = get_object_or_404(UserProfile, user=request.user)
        if answer and answer.text:
            form = AIChatForm(request.POST)
            if form.is_valid():
                data = Chat()
                data.user = profile
                data.question = request.POST.get('ask')
                data.answer = answer.text.replace('*', ' ',).strip()
                data.ip = request.META.get('REMOTE_ADDR')
                data.save()
                cleaner()
                return redirect(url)

def cleaner():
    trashes = list(Chat.objects.all())
    while len(trashes) > 5:
        trash = trashes[0]
        trash.delete()
        trashes.remove(trash)
    return redirect('chatWithAI')
