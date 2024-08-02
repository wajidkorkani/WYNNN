from email.mime import image
from sqlite3 import Timestamp
from unicodedata import category
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    time_stamp = models.DateTimeField(auto_now=True)
    slug = models.SlugField(default='save')
    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.user.username

class UserPost(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    capution = models.CharField(max_length=2000)
    likes = models.ManyToManyField(User, related_name="Post_likes", blank=True)
    time_stamp = models.DateTimeField(auto_now=True)



class Blog(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    title = models.CharField(max_length=200, default='Title')
    text = models.TextField()
    category = models.CharField(max_length=200, null=True, blank=True) 
    likes = models.ManyToManyField(User, related_name="Blog_likes",blank=True)
    time_stamp = models.DateTimeField(auto_now=True)

class BlogComment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    comment = models.CharField(max_length=500, blank=True)
    ip = models.CharField(max_length=20, blank=True)
    time_stamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

class BlogCommentReply(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    blog_comment = models.ForeignKey(BlogComment, on_delete=models.CASCADE)
    reply = models.CharField(max_length=500, blank=True)
    ip = models.CharField(max_length=20, blank=True)
    time_stamp = models.DateTimeField(auto_now=True)

