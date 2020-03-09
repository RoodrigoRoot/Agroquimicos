from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import logging

logging.basicConfig(
    level=logging.DEBUG
)


class LoginForm(forms.Form):   
    username = forms.CharField(label="Nombre de Usuario" ,help_text="Ingrese su nombre de usuario", 
    widget=forms.TextInput(attrs={
        "placeholder":"Ingrese su nombre de usuario"
    })
    )
    password = forms.CharField(label="Contraseña", help_text="Ingrese su contraseña", widget=forms.PasswordInput(attrs={
        "placeholder":"Ingrese su Contraseña"
    }))

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


class RegisterForm(forms.Form):

    username = forms.CharField(help_text="No incluir ñ, acentos Ó %, $, #", max_length=20, label="Nombre de Usuario",
    widget=forms.TextInput(attrs={
        "placeholder":"Ingrese su nombre de usuario"
    }))
    
    name = forms.CharField(help_text="Ingrese el nombre(s)*", label="Nombre de la persona", widget=forms.TextInput(attrs={
        "placeholder":"Ingrese el nombre(s)"
    }))
    
    last_name = forms.CharField(max_length=250,help_text="Ingrese los apellidos*", label="Apellidos de la persona",widget=forms.TextInput(attrs={
        "placeholder":"Ingrese los apellidos"
    }))
    
    email = forms.EmailField(help_text="Ingrese un correo electronico", label="Correo Electronico")
    
    password = forms.CharField(help_text="Ingrese una contraseña", label="Contraseña", widget=forms.PasswordInput(attrs={
        "placeholder":"Ingrese una contraseña"
    }))

    password2 = forms.CharField(help_text="Repita la contraseña", label="Repita la contraseña", widget=forms.PasswordInput(attrs={
        "placeholder":"Ingrese otra vez la misma contraseña"
    }))

    def clean_username(self):
        username = str.lower(self.cleaned_data['username'])
        if len(username) < 3:
            raise ValidationError("El usuario no puede tener menos de 3 letras")
        if User.objects.filter(username=username).exists():
            raise ValidationError("Ese usuario ya esta registrado")
        return username

    def clean_name(self):
        name = str.lower(self.cleaned_data['name']) 
        return name
    
    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        return last_name
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este correo ya esta registrado")
        return email
    
    def clean_password(self):
        password = self.cleaned_data['password']
        return password
    
    def clean_password2(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if not password == password2:
            raise ValidationError("Las contraseñas no son iguales, por favor vuelva a escribirlas")
        return password
