from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm , TextInput
from django import forms
from .models import AllUser


class AllUserCreationForm(UserCreationForm):
    class Meta:
        model = AllUser
        fields = ('name','email','phone','status' )



class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label='Nom d’utilisateur')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')