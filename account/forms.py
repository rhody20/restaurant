from dataclasses import field, fields
from pyexpat import model
from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields =('username','first_name','last_name','email','password1','password2')




class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields =('phone_number','addr')



class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')



class TodoForm(forms.ModelForm):
    class Meta:
        model=mytodos
        fields =('task',)
