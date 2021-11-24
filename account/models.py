from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Follower (models.Model) :
    user = models.OneToOneField(User,related_name='user',on_delete=models.CASCADE)
    followers = models.ManyToManyField(User,related_name='followers',blank=True)
    
    def __str__(self) : 
        return self.user.username

class profile (models.Model) :
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    fg = models.ImageField(upload_to='static/fg/',default='static/fg/anon.png')
    is_online = models.BooleanField(default=False)

    def __str__ (self) :
        return self.user.username