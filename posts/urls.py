from django.urls import path
from . import views
from . import api

urlpatterns = [
    path('manage-posts/',views.posts,name='posts'),
    path('edit/<pk>',views.Edit.as_view(),name='edit_posts'),
    path('del/<pk>',views.DelPosts,name='delete'),
    path('love-post/<int:postid>',views.lovePost,name='love'),
    path('add-comment/<int:postid>',views.comment,name='comment'),
    path('view-comments/<int:postid>/',views.view_comments,name='view_comments'),
    path('view-comments/del/<int:comment>',views.Delete_Comments,name='del_comment'),
    path('view-comments/update/<int:comment>',views.update_comment,name='update_comment'),
    # notifications
    path('notifications/',views.view_notify,name='noti'),
    path('notifications/delete/<int:id>',views.del_notify,name='del_noti'),
    

    # api
    path('api/posts/',api.listPost,name='listpost')

]