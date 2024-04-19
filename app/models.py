from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import ModelForm , TextInput



class AllUser(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='groups_related',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_permissions_related',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
    username = None
    #is_verified = models.BooleanField(default=False)
    date_inscription = models.DateTimeField(auto_now=True)
    name = models.CharField("Entrer votre nom et prenom", max_length=80)
    email = models.EmailField( max_length=254, unique=True)
    phone = models.CharField('Telephone', max_length=50)
    status = models.CharField(max_length=50, default = '1')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "AllUser"
        verbose_name_plural = "AllUsers"

    def __str__(self):
        return self.name