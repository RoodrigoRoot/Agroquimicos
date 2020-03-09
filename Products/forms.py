from django import forms
import datetime as dt
from django.core.exceptions import ValidationError
from .models import *

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("name", "description", "category")
        labels = {
            "name":"Nombre del Producto",
            "description":"Descripción del Producto",
        }
        widgets = {
          'description': forms.Textarea(attrs={'rows':2, 'cols':20}),
        }

class DetailsProductForm(forms.ModelForm):
    class Meta:
        model = DetailProduct
        fields = ("price", "expiration")
        labels = {
            "price": "Precio del Producto"
        }
        widgets = {
          'expiration': forms.TextInput(attrs={"type":"date"}),
        }                                          

    def clean_expiration(self):
      expiration = self.cleaned_data["expiration"]
      if expiration < dt.date.today():
        raise ValidationError("La fecha de expiración no puede ser menor a hoy")
      return expiration

class AddWarehouseForm(forms.ModelForm):
  class Meta:
    model = Warehouse
    fields = ("quantity",)
