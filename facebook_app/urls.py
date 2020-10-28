from django.urls import path
from .views import *

app_name = 'facebook_app'

urlpatterns = [

    path('registration/',UserRegistration.as_view(),name='registration'),
    path('login/',UserLogin.as_view(),name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('user-dashboard/<int:pk>',UserDashboard.as_view(),name='dashboard'),
    path('add-post/',UserAddPost.as_view(),name='add_post',),
    path('my-post/',UserPostList.as_view(),name='my_post'),
    path('post-delete/<post_id>',UserPostDelete.as_view(),name='post_delete'),
    path('friends/',FriendList.as_view(),name='friends'),
    path('change-friends/<int:pk>',change_friends,name='change_friends'),
    path('friend-request/',FriendRequests.as_view(),name='friend_request'),
    path('add-friends/<int:pk>',make_friends,name='add_friends'),
    path('my-friends/',MyFriends.as_view(),name='my_friends'),
   


]