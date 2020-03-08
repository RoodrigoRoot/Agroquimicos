from django.shortcuts import render
from django.views import View

from .models import *
# Create your views here.

class ProductView(View):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        return render(request, 'product/product.html', locals())

class AddProductView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'product/addProduct.html', locals())

class DeleteProductView(View):
    
    @property
    def slug(self):
        return self.kwargs['slug']

    def get(self, request, *args, **kwargs):
        name = Product.objects.filter(slug=self.slug).first()
        return render(request, 'product/deleteProduct.html', locals())


class UpdateProductView(View):
    
    def get(self, request, *args, **kwargs):
        
        return render(request, 'product/updateProduct.html', locals())

class SearchProductView(View):
    def get(self, request, *args, **kwargs):
        print(request.GET)
        return render(request, 'product/searchProduct.html', locals())