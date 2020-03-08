from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import logging

logging.basicConfig(
    level=logging.DEBUG
)


class LoginForm(forms.Form):   
    username = forms.CharField(label="Nombre de Usuario" ,help_text="Ingrese su nombre de usuario")
    password = forms.CharField(label="Contraseña", help_text="Ingrese su contraseña", widget=forms.PasswordInput())

    def clean_username(self):
        username = str.lower(self.cleaned_data['username'])
        if not User.objects.filter(username=username).exists():
            raise ValidationError("Usuario o Contraseña incorrectos")
        return username
    

    def clean_password(self):
        username = str.lower(self.data['username'])
        password = self.cleaned_data['password']
        user = User.objects.filter(username=username).first()
        if user and not user.check_password(password):
            raise ValidationError("Usuario o Contraseña incorrectos")
        return password

