from django.urls import path
from .views import UserLogin, UserRegistration

app_name = 'facebook_app'

urlpatterns = [

    path('page/',UserLogin.as_view(),name='login'),
    path('registration/',UserRegistration.as_view(),name='registration'),
    path('login/',UserLogin.as_view(),name='login'),

]