from django.urls import path
from .views import UserLogin, UserRegistration, UserDashboard,UserPostList,UserLogout, UserPostView

app_name = 'facebook_app'

urlpatterns = [

    path('registration/',UserRegistration.as_view(),name='registration'),
    path('login/',UserLogin.as_view(),name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('user-dashboard/<int:pk>',UserDashboard.as_view(),name='dashboard'),
    path('post/',UserPostView.as_view(),name='post',),
    path('my-post/',UserPostList.as_view(),name='my_post'),


]