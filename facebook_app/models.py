import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Registration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob= models.DateField(null=True, blank=True)
    def __str__(self):
        return str(self.user)

class UserPost(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.CharField(max_length=100)