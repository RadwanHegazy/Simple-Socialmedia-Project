from django import forms
from django.contrib.auth.models import User
from .models import Post, Comment

class AddPosts (forms.ModelForm) :
    class Meta :
        model = Post
        fields = ['title','video','image']

class AddComment (forms.ModelForm) :
    class Meta :
        model = Comment
        fields = ['comment']