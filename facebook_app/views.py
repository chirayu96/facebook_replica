import smtplib
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import *
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.models import User
from .models import Registration
from django.conf import settings 
from django.core.mail import send_mail 

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
            return redirect("/page/")
            # return request(request,'facebook/registration.html',{'form':form})


class UserLogin(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request,"facebook/registration.html",{"login_form":form})


    def post(self, request):
        form = UserLoginForm(request.POST or None)
        try:
            if form.is_valid():
                # import pdb; pdb.set_trace()
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                user = authenticate(username=username, password=password)
                if user is not None:
                    user = Registration.objects.get(user=user)
                    return redirect("/page/")
                else:
                    msg="Incorect Username or Password"
                    return render(request,"facebook/registration.html",{'msg': msg})
           
        except Exception as e:
                return render(request,"facebook/registration.html",{'error':e,'form':form})