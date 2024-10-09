from django.urls import path
from Core.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    # Post urls section
    path('home/', home, name='home'),
    path('upload$post/<int:pk>/', Create_User_Post.as_view(), name='create_user_post'),
    path('<int:pk>/post/like/', post_likes, name='post_likes'),
    path('<slug:slug>/posts/<int:pk>/', current_user_posts, name='current_user_posts'),
    path('delete-post/<int:pk>/', Delete_Post.as_view(), name='delete_post'),

    # Profile section
    path('create-user-profile/', Create_User_Profile.as_view(), name='Create_User_Profile'),
    path('changeImage<int:pk>', Change_User_Profile_Image.as_view(), name="change_image"),
    path('me/', current_user_profile, name='current_user_profile'),
    path('delete-profile/<int:pk>/', Delete_Profile.as_view(), name='delete_profile'),
    path('update-profile/<int:pk>/', Update_Profile.as_view(), name='update_profile'),

    # Blog urls section
    path('blog/<int:pk>/', Create_Blog.as_view(), name='create_blog'),
    path('blogs/', all_blogs, name='all_blogs'),
    path('<int:pk>/blog/', blog_about_page, name='blog_about_page'),
    path('submit_review/<int:blog_id>/', submit_blog_review, name='submit_review'),
    path('comment/<int:pk>', blog_comment_about_page, name='blog_comment_about_page'),
    path('comment/<int:comment_id>/reply', submit_comment_reply, name='submit_comment_reply'),
    path('<slug:slug>/blogs/<int:pk>/', current_user_blogs, name='current_user_blogs'),
    path('delete-blog/<int:pk>/', Delete_Blog.as_view(), name='delete_blog'),

    # All users urls section
    path('<slug:slug>/<int:pk>/blogs/', all_users_blogs, name='all_users_blogs'),
    path('<slug:slug>/<int:pk>/posts/', all_users_posts, name='all_users_posts'),
    path('all-users/<int:pk>/profile/page', all_users_profile_page, name='all_users_profile_page'),

    # Searchbar url
    path('search/', searchbar, name='searchbar'),

    # messageSection
    path('ai', AIChat, name='AIChat'),
    path('chatWithAI', chatWithAI, name='chatWithAI')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
