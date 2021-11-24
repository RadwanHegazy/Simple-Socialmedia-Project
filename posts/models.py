from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import NullBooleanField
# Create your models here.

class Post (models.Model) :
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_posts')
    title = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    lovers = models.ManyToManyField(User, related_name='lovers',blank=True)
    image = models.ImageField(upload_to='static/posts/',null=True,blank=True)
    video = models.FileField(upload_to='static/posts-videos/',null=True,blank=True)
    
    def __str__(self) :
        return str(self.title)


class Comment (models.Model) :
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_comment')
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='post_comment')
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return f"{self.user.username} -> {self.post.title}"


class Notification (models.Model) : 
    from_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='sender')
    to_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='reciver')
    msg = models.TextField()
    date = models.DateTimeField(auto_now_add=True)