import smtplib
from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import *
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.models import User
from .models import Registration,UserPost, Friends
from django.conf import settings 
from django.core.mail import send_mail 
from django.contrib.auth import authenticate, login ,logout
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponseRedirect


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


class UserAddPost(View): 
    def get(self, request):
        post_list = UserPost.objects.filter(user=request.user)
        return render(request, 'facebook/facebook.html',{'post_list':post_list})

    def post(self,request):
        try:
            user = UserPost.objects.create(user=request.user,post=request.POST['post'])
            user.save()
            return JsonResponse({'status':True, 'message' : "Successfully created"})
        except Exception as e:
            return JsonResponse({'status':False, 'message' : str(e)})
            # return redirect("/user-dashboard/")
       

class UserPostDelete(View):
    def get(self,request,post_id):
        form = UserLoginForm()
        user_post_id = UserPost.objects.get(id=post_id)
        user_post_id.delete()
        return HttpResponseRedirect("/user-dashboard/"+str(request.user.id))
        # return redirect("/dashboard/")
        # return render(request,'facebook/facebook.html',{'message': 'Deleted successfully!','form':form})


class FriendList(View):
    def get(self,request):
        queryset = User.objects.all()
        return render(request,'facebook/friends.html',{'queryset':queryset})
        # user = User.objects.get(id=user.id)
        # user_obj = get_object_or_404(User, id=pk)
        



def change_friends(request, pk):
    friend = User.objects.get(pk=pk)
    add_obj = Friends.objects.create(user=request.user,
                friend=friend,
                status=2),
    return HttpResponseRedirect("/friends/")
    # return redirect('/friends/')
    # if operation == 'add':
    #     Friend.make_friend(request.user, friend)
    # elif operation == 'remove':
    #     Friend.lose_friend(request.user, friend)
    # return redirect('/friends/')



# def friend_request(self,request):
#     import pdb; pdb.set_trace()
#     request_user = Friends.objects.filter(user=request.user,status=2)
#     return True
#     # return render(request,'facebook/friend_request.html')

class FriendRequests(View):
    def get(self,request):
        pending_request = Friends.objects.filter(friend=request.user,status=2)
        return render(request,'facebook/friend_request.html',{'pending_request':pending_request})


def make_friends(request,pk):
    friend = Friends.objects.get(pk=pk,status=2)
    friend.status=1
    # rqst_status =friend.status(commit=1)
    friend.save()
    return redirect('/friend-request/')


class MyFriends(View):
    def get(self,request):
        friend_obj = Friends.objects.filter(friend=request.user,status=0)
        return render(request,'facebook/my_friend.html',{'friend_obj':friend_obj})