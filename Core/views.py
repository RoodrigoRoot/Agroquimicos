from django.shortcuts import render
from django.views import View
from .forms import *
# Create your views here.

class LoginView(View):
    
    def get(self, request, *args, **kwargs):
        forms = LoginForm()
        return render(request, 'core/login.html', locals())