from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm , TextInput
from django import forms
from .models import *


class AllUserCreationForm(UserCreationForm):
    class Meta:
        model = AllUser
        fields = ('name','email','phone','status' )



class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label='Nom d’utilisateur')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')


class EventForm(forms.Form):
    class Meta:
        model = Event
        fields = ('date_debut', 'name', 'user','description','is_free', 'is_narmal', 'is_vip', 'is_premium')
    

class TicketForm(forms.Form):
    class Meta:
        model = Ticket
        fields = ('name', 'event', 'price', 'quantite', 'rang')
    
