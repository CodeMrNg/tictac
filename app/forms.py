from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm , TextInput
from django import forms
from .models import *


from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import AllUser

class AllUserCreationForm(UserCreationForm):
    class Meta:
        model = AllUser
        fields = ('profil','name', 'email', 'phone', 'status', 'password1', 'password2')  # Ajout des champs de mot de passe

    # Définition des champs du formulaire avec leurs attributs
    profil = forms.FileField(
        label='',
        widget=forms.FileInput(attrs={'class': 'profile-img-file-input', 'accept': 'image/*', 'required': True, 'data-max-file-size': '3MB','style':'display:none'})
    )
    name = forms.CharField(
        label='Nom et Prénom', 
        max_length=80,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrer votre nom et prénom'}),
    )
    email = forms.EmailField(
        label='Email', 
        max_length=254,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre email'}),
    )
    phone = forms.CharField(
        label='Téléphone', 
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre numéro de téléphone'}),
    )
    status = forms.CharField(
    label='Status',
    max_length=50,
    widget=forms.HiddenInput(attrs={'value': '1'}),  # Utilisation du widget HiddenInput pour cacher le champ
    initial='1',  # Valeur initiale du champ (non affichée)
)

    password1 = forms.CharField(
        label='Mot de passe',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre mot de passe'}),
    )
    password2 = forms.CharField(
        label='Confirmation du mot de passe',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmez votre mot de passe'}),
    )

    # Fonction de validation des mots de passe
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Les mots de passe ne correspondent pas.")
        return password2

    # Sauvegarde des données dans le modèle AllUser
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label='Nom d’utilisateur')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('place_number', 'banniere', 'date_debut', 'name', 'location', 'user', 'description', 'is_free', 'is_normal', 'is_vip', 'is_premium')
        widgets = {
            'place_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Numéro de place'}),
            
            'date_debut': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de l\'événement'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lieu'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description de l\'événement','rows':"3"}),
            'is_free': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_normal': forms.NumberInput(attrs={'class': 'form-control',}),
            'is_vip': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_premium': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  
        
        super(EventForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['user'].initial = user  # Affecter l'utilisateur connecté au champ 'user' du formulaire
            self.fields['user'].widget = forms.HiddenInput()

from django.forms import ModelForm, TextInput, NumberInput

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ('name', 'event', 'price', 'quantite', 'rang')
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom du ticket'}),
            'event': TextInput(attrs={'class': 'form-control', 'placeholder': 'Événement'}),
            'price': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Prix'}),
            'quantite': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantité'}),
            'rang': TextInput(attrs={'class': 'form-control', 'placeholder': 'le numero qui fera le payement'}),
        }

    
class QuantForm(forms.Form):
    quant = forms.CharField(max_length=63, label='')