from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.generic.edit import FormMixin
from .models import Post, Comment, Notification
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.views import reverse_lazy
from .forms import AddPosts, AddComment
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


def del_notify (request , id) :
    getNoti = get_object_or_404(Notification, id=id)
    getNoti.delete()
    return redirect('noti')

def view_notify (request) :

    data = Notification.objects.filter(to_user=request.user).order_by('-date')
    return render(request,'notifi.html',{'nots':data})


def view_comments (request, postid) :
    getPost = get_object_or_404(Post,pk=postid)
    coms = Comment.objects.filter(post=getPost).all().order_by('-date')
    return render(request,'view_comment.html',{'post':getPost,'comments':coms})

# @login_required
def lovePost (request, postid) :
    getPost = get_object_or_404(Post,pk=postid)
    if request.user.is_authenticated :
        if request.user in getPost.lovers.all() :
            getPost.lovers.remove(request.user)
            liked = False
        else :
            getPost.lovers.add(request.user)
            msg = f"{request.user} liked your post : {getPost.title}"
            Notification.objects.create(from_user=request.user,to_user=getPost.user,msg=msg)
            liked = True
        data = {
            'value' : getPost.lovers.all().count(),
            'liked' : liked,
            'loged' : True
            }
    else :
        data = {'loged':False}
    return JsonResponse(data, safe=False)
    
    # url = request.META['HTTP_REFERER']
    # return redirect(url)

@login_required
def comment (request, postid) :
    post = get_object_or_404(Post,id=postid)
    com = request.POST['comment']
    user = request.user
    Comment.objects.create(post=post,user=user,comment=com).save()
    msg = f"{request.user} commented in your post : {post.title}"
    Notification.objects.create(from_user=request.user,to_user=post.user,msg=msg)
    return JsonResponse(data={'message':'comment has been sent !'})


@login_required
def posts (request) :
    content = request.POST.get('post_cont')
    video = request.FILES.get('video')
    image = request.FILES.get('image')
    Post.objects.create(user=request.user, title=content,video=video,image=image)
    return redirect('home')


class Edit (UpdateView) :
    model = Post
    fields = ['title','image','video']
    success_url = reverse_lazy('profile')
    template_name = 'edit_posts.html'

@login_required
def DelPosts (request, pk) :
    post = get_object_or_404(Post,pk=pk)
    Post.objects.get(pk=post.pk).delete()
    return redirect('profile')

@login_required
def Delete_Comments (reqeust, comment) :
    Comment.objects.get(id=comment).delete()
    path = reqeust.META['HTTP_REFERER']
    return redirect(path)


@login_required
def update_comment (request, comment) :
    msg = request.POST.get('cmt')
    com = Comment.objects.get(id=comment)
    com.comment = msg
    com.save()
    return redirect(request.META['HTTP_REFERER'])