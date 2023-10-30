from django.urls import path 
from Core.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    # Post urls section
    path('home/', home, name='home'),
    path('<slug:slug>/post/<int:pk>/', Create_User_Post.as_view(), name='create_user_post'),
    path('<int:pk>/post/like/', post_likes, name='post_likes'),
    path('<slug:slug>/posts/<int:pk>/', current_user_posts, name='current_user_posts'),

    # Profile section
    path('create-user-profile/', Create_User_Profile.as_view(), name='Create_User_Profile'),
    path('me/', current_user_profile, name='current_user_profile'),

    # Blog urls section
    path('<slug:slug>/blog/<int:pk>/', Create_Blog.as_view(), name='create_blog'),
    path('blogs/', all_blogs, name='all_blogs'),
    path('<int:pk>/blog/', blog_about_page, name='blog_about_page'),
    path('submit_review/<int:blog_id>/', submit_blog_review, name='submit_review'),
    path('comment/<int:pk>', blog_comment_about_page, name='blog_comment_about_page'),
    path('comment/<int:comment_id>/reply', submit_comment_reply, name='submit_comment_reply'),
    path('<slug:slug>/blogs/<int:pk>/', current_user_blogs, name='current_user_blogs'),

    # All users urls section 
    path('<slug:slug>/<int:pk>/blogs/', all_users_blogs, name='all_users_blogs'),
    path('<slug:slug>/<int:pk>/posts/', all_users_posts, name='all_users_posts'),
    path('all-users/<int:pk>/profile/page', all_users_profile_page, name='all_users_profile_page'),

    # Searchbar url 
    path('search/', searchbar, name='searchbar'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
