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


def logout_view(request):
    logout(request)
    return redirect(reverse("home"))