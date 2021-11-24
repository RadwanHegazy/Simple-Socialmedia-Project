from django.contrib import admin
from .models import Follower, profile
# Register your models here.

admin.site.register(profile)
admin.site.register(Follower)