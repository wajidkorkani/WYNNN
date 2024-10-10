from django import forms
from .models import *

class CommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['comment']
class ReplyForm(forms.ModelForm):
    class Meta:
        model = BlogCommentReply
        fields = ['reply']

class PostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ['comment']

class AIChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['question']