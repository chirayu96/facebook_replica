from django.shortcuts import render
from django.views.generic import *

class UserLogin(View):
	def get(self,request):
		return render(request,'facebook/facebook.html')
