from django.contrib import admin
from .models import Registration,UserPost,Friends

# Register your models here.
admin.site.register(Registration)
admin.site.register(UserPost)
admin.site.register(Friends)