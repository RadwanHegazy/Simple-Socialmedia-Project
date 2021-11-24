from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import SignupForm, AddImage
from django.contrib.auth.views import auth_login
from django.contrib.auth.models import User
from django.contrib.auth.views import reverse_lazy
from django.views.generic import UpdateView
from .models import Follower, profile as Profile
from django.contrib.auth.decorators import login_required
from posts.models import Post, Notification
from posts.forms import AddComment, AddPosts
import datetime


def find_people (request) :
    if request.method == 'POST' :
        user = request.POST.get('friend')
        users = User.objects.filter(first_name=user).all()
        list = []
        me = request.user
        for i in users :
            list.append(i)
        if me in list :
            list.remove(me)
        return render (request, 'search.html',{'users':list})

    return render(request,'search.html')

def home (request) :
    posts = Post.objects.all().order_by('-date')
    form = AddComment()
    allusers = User.objects.all()
    
    if request.user.is_authenticated :
        me = request.user
        my_users = []
        for i in allusers :
            my_users.append(i)
        my_users.remove(me)
        getFollowers = get_object_or_404(Follower,user=request.user).followers.all()
        getPosts = Post.objects.filter(user=request.user).all()
        return render(request,'home.html',{'posts':posts,'allusers':my_users,'form':form,'UserPosts':getPosts,'fols':getFollowers})
        

    return render(request,'home.html',{'posts':posts,'allusers':allusers,'form':form})


@login_required
def UpdatePhoto (request,pk) :
    form = AddImage()
    if request.method == "POST" :
        form = AddImage(request.FILES)
        if form.is_valid() :
            data = Profile.objects.get(user=request.user)
            data.fg = request.FILES['fg']
            data.save()
            
            return redirect('profile')
    return render(request,'UpdatePhoto.html',{'form':form})


@login_required
def DeletePhoto (request, pk) :
    getimage = get_object_or_404(User,pk=pk)
    data = Profile.objects.get(user=getimage)
    data.fg = 'static/fg/anon.png'
    data.save()
    return redirect('profile')

@login_required
def follow (request, pk) :
    getUser = get_object_or_404(User,pk=pk)
    user = User.objects.get(username=getUser.username)
    followers = Follower.objects.get(user=user)
    if request.user in followers.followers.all() :
        followers.followers.remove(request.user)
    else :
        followers.followers.add(request.user)
        msg = f'{request.user} started following you '
        Notification.objects.create(from_user=request.user,to_user=user,msg=msg)

    return redirect('view_user',user.username)

@login_required 
def profile (request) :
    user = request.user
    followers = Follower.objects.get(user=user)
    posts = Post.objects.filter(user=user).all().order_by('-date')
    return render(request,'profile.html',{'followers':followers.followers,'posts':posts})


def View_users (request, username) :
    getUser = get_object_or_404(User,username=username)
    if request.user == getUser :
        return redirect('profile')
    followers = Follower.objects.get(user=getUser)
    posts = Post.objects.filter(user=getUser).all()
    return render(request,'view_user.html',{'Theuser':getUser,'followers':followers.followers,'posts':posts})


class UpdateUser (UpdateView) :
    model = User
    fields = ['username','email','first_name','last_name']
    success_url = reverse_lazy('profile')
    template_name = 'update_user.html'

def signup (request) :
    form = SignupForm()
    if request.method == "POST" :
        form = SignupForm(request.POST)
        if form.is_valid() :
            user = form.save()
            auth_login(request,user=user)
            Follower.objects.create(user=user).save()
            Profile.objects.create(user=user).save()
            return redirect('home')

    return render(request, 'signup.html',{'form':form})