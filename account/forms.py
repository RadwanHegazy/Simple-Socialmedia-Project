from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import profile as Prof

class SignupForm (UserCreationForm) :
    email = forms.EmailField()
    class Meta :
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']

class AddImage (forms.ModelForm) :
    class Meta :
        model = Prof
        fields = ['fg']