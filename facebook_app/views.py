import smtplib
from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import *
from .forms import UserRegistrationForm, UserLoginForm,UserPostForm
from django.contrib.auth.models import User
from .models import Registration,UserPost
from django.conf import settings 
from django.core.mail import send_mail 
from django.contrib.auth import authenticate, login ,logout
from django.shortcuts import get_object_or_404
# class UserLogin(View):
#     def get(self,request):
#         return render(request,'facebook/facebook.html')


class UserRegistration(View):
    def get(self,request):
        form = UserRegistrationForm()
        return render(request,'facebook/registration.html',{'form':form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create(
                first_name=form.data['first_name'],
                last_name=form.data['last_name'],
                username=form.data['username'],
                email=form.data['email'])
            user.set_password(form.data['password'])
     
            subject = 'welcome to GFG world'
            message = f'Hi {user.username}, thank you for registering in geeksforgeeks.'
            email_from = settings.EMAIL_HOST_USER 
            recipient_list = [user.email,] 
            send_mail( subject, message, email_from, recipient_list )
            user.save()
           
            registration_obj = Registration.objects.create(user=user,
                dob=form.data['dob'])
            return redirect("/login/")
            # return request(request,'facebook/registration.html',{'form':form})


class UserLogin(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request,"facebook/login.html",{"login_form":form})


    def post(self, request):
        form = UserLoginForm(request.POST or None)
        try:
            if form.is_valid():
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(username=username, password=password)
                login(request, user)
                if user is not None:
                    user = User.objects.get(pk=user.id)
                    return redirect("/user-dashboard/"+str(user.id))
                else:
                    msg="Incorect Username or Password"
                    return render(request,"facebook/login.html",{'msg': msg})
           
        except Exception as e:
                return render(request,"facebook/login.html",{'error':e,'login_form':form})

class UserDashboard(View):
    def get(self, request,pk):
        user_obj = get_object_or_404(User, id=pk)
        post_list = UserPost.objects.filter(user=request.user)
        return render(request, 'facebook/facebook.html',{'user_obj':user_obj,'post_list':post_list})

class UserPostList(View):
    def get(self,request):
        post_list = UserPost.objects.filter(user=request.user)
        return render(request,'facebook/user_post_list.html',{'post_list':post_list})
      
       
class UserLogout(View):
    def get(self,request):
        logout(request)
        messages.info(request,"Logout Successfully!!!!!!!")
        return redirect("/login/")


# class UserPostView(View): 
#     def get(self, request):
#         post_list = UserPost.objects.filter(user=request.user)
#         return render(request, 'facebook/facebook.html',{'post_list':post_list})

    # def post(self,request):
    #     form = UserPostForm(request.POST)
    #     if form.is_valid():
    #         user = UserPost.objects.create(post=form.data['post'])
    #         user.save()
    #         return redirect("/user-dashboard/")
    #     else:
    #         form=UserPostForm()
    #         return render(request,"facebook/dashboard.html")
