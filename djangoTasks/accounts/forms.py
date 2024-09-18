from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        labels = {
            "username": "Username",
            'first_name': "First Name",
            'last_name': "Last Name",
            'email': "Email",
            'password': "Password"
        }
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"}),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"class": "form-control"}))