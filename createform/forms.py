from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2']



class loginform(forms.Form):
    username = forms.CharField(max_length = 200)
    password = forms.CharField(widget = forms.PasswordInput())