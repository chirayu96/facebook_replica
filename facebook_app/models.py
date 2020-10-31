import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Registration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob= models.DateField(null=True, blank=True)
    
    def __str__(self):
        return str(self.user)



class Friends(models.Model):
    REQUEST_STATUS = ((0, 'Accepted'), (1, 'Rejected'), (2, 'Pending'))
    
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user')
    friend = models.ForeignKey(User, on_delete=models.CASCADE,related_name='friend')
    status = models.SmallIntegerField(choices=REQUEST_STATUS,default=2)
    
    def __str__(self):
        return str(self.user)

class UserPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.CharField(max_length=100)
    friend_post = models.ForeignKey(Friends, on_delete=models.CASCADE,related_name='friends_post',null=True)

# class AcceptRequest(models.Model):

#     user  = models.ManyToManyField(User)
#     current_user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='owner', null=True)
#     