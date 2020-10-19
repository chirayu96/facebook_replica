from django.urls import path
from .views import UserLogin

app_name = 'facebook_app'

urlpatterns = [

path('',UserLogin.as_view(),name='login')

]