from django.urls import path
from . import views
from django.contrib.auth import views as Vs

urlpatterns = [
    path('',views.home,name='home'),
    path('find-people/',views.find_people,name='FindPeople'),
    path('signup/',views.signup,name='signup'),
    path('logout/',Vs.LogoutView.as_view(),name='logout'),
    path('login/',Vs.LoginView.as_view(template_name='login.html'),name='login'),
    path('change-password/',Vs.PasswordChangeView.as_view(template_name='change_password.html'),name='pas'),
    path('change-password/done/',Vs.PasswordChangeDoneView.as_view(template_name='change_password_done.html'),name='password_change_done'),
    path('profile/',views.profile,name='profile'),
    path('profile/update/<pk>',views.UpdateUser.as_view(),name='update_user'),
    path('<str:username>/',views.View_users,name='view_user'),
    path('follow/<int:pk>/',views.follow,name='follow'),
    path('update-profile-image/<int:pk>/',views.UpdatePhoto,name='update_img'),
    path('delete-profile-image/<int:pk>/',views.DeletePhoto,name='del_img'),
]