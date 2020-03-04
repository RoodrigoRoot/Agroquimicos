from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
#    username = forms.CharField(label="Usuario", help_text="Ingrese su nombre de usuario", widget=forms.TextInput(
#        attrs={
#            "class": "form-control",
#            "id":"InputUsername",
#            "aria-describedby":"emailHelp",
#        }
#    ))
    
    username = forms.CharField(label="Nombre de Usuario" ,help_text="Ingrese su nombre de usuario")
    password = forms.CharField(label="Contraseña", help_text="Ingrese su contraseña", widget=forms.PasswordInput())
    
    
