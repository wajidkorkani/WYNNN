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