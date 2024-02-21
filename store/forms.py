from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm): 
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    #Styles Django's CustomerUserCreationForm, loops through the fields in login_retister.html
    #Allowing you to put your own placeholders in the form
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control','placeholder':'Enter username...'})
        self.fields['email'].widget.attrs.update({'class': 'form-control','placeholder':'Enter email...'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control','placeholder':'Enter password...'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control','placeholder':'Confirm password...'})
