import datetime
from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.Form):

    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    username = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    # email = froms.CharField(max_length=50)
    password = forms.CharField(max_length=10)
    dob = forms.DateField(initial=datetime.date.today())

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class':"inputbody in1",'placeholder':'First Name'})
        self.fields['last_name'].widget.attrs.update({'class':"inputbody in1",'placeholder':'Last Name'})
        self.fields['username'].widget.attrs.update({'class':"inputbody in2",'placeholder':'Username'})        
        self.fields['email'].widget.attrs.update({'class':"inputbody in2",'placeholder':'Email'})
        self.fields['password'].widget.attrs.update({'class':"inputbody in2",'placeholder':'New Password'})
        self.fields['dob'].widget.attrs.update({'class':"inputbody in2",'placeholder':'Date of Birth'})


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':"row1", 'label':'Email or Phone'})
        self.fields['password'].widget.attrs.update({'class':"row1",'label':'Password'})