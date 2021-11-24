from re import I
from .serializer import PostSerializer
from .models import Post
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def listPost (requset) :
    all_posts = Post.objects.all().order_by('-date')
    data = PostSerializer(all_posts, many=True).data
    return Response({'data':data})