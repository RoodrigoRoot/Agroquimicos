from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name="home"),
    path('entrar/', LoginView.as_view(), name="login"),
    path('registrar/', RegisterView.as_view(), name="register"),
    path('salir/', logout_view, name="logout"),
]
