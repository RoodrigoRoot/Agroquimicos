from django.shortcuts import render, redirect, reverse
from django.views import View
from django.contrib.auth import logout, authenticate, login
import logging

from .forms import *

logging.basicConfig(
    level=logging.DEBUG
)

# Create your views here.

class LoginView(View):
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse("home"))
        else:
            forms = LoginForm()
        return render(request, 'core/login.html', locals())
    
    def post(self, request, *args, **kwargs):
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("home"))
        return render(request, 'core/login.html', locals())

class IndexView(View):

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse("login"))
        return render(request, 'core/index.html', locals())


class RegisterView(View):

    def get(self, request, *args, **kwargs):
        forms = RegisterForm()
        return render(request, 'core/register.html', locals())

    def post(self, request, *args, **kwargs):
        forms = RegisterForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            name = forms.cleaned_data['name']
            last_name = forms.cleaned_data['last_name']
            email = forms.cleaned_data['email']
            password = forms.cleaned_data['password']
            user = User.objects.create_user(
                username=username,
                email=email,
                last_name=last_name,
                first_name=name,
                password=password)
            if user is not None:
                logging.info("User created")
            else:
                logging.info("Problems with User") 
        return render(request, 'core/register.html', locals())

def logout_view(request):
    logout(request)
    return redirect(reverse("home"))