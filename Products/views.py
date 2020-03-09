from django.shortcuts import render, reverse, redirect
from django.views import View
from .forms import *
from .models import *
import logging
# Create your views here.

logging.basicConfig(
    level=logging.DEBUG
)

class ProductView(View):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        
        return render(request, 'product/product.html', locals())

class AddProductView(View):
    def get(self, request, *args, **kwargs):
        forms = AddProductForm()
        form = DetailsProductForm()
        fo = AddWarehouseForm()
        return render(request, 'product/addProduct.html', locals())
    
    def post(self, request, *args, **kwargs):
        try:
            forms = AddProductForm(request.POST)
            form = DetailsProductForm(request.POST)
            if forms.is_valid() and form.is_valid():
                name_product = forms.cleaned_data['name']
                description = forms.cleaned_data['description']
                category = forms.cleaned_data['category']
                user = request.user
                product = Product.objects.create(
                    name=name_product,
                    description=description,
                    category=category,
                    user=user,
                )
                if product is not None:
                    expiration = form.cleaned_data['expiration']
                    price = form.cleaned_data['price']
                    dtp = DetailProduct.objects.create(
                        product=product,
                        expiration=expiration,
                        price=price,
                        user=request.user
                    )
                    alerts = True
        except Exception as e:
            logging.debug("Problems with to create product", e)
            return -1
        return render(request, 'product/addProduct.html', locals())

class DeleteProductView(View):
    
    @property
    def slug(self):
        return self.kwargs['slug']

    def get(self, request, *args, **kwargs):
        name = Product.objects.filter(slug=self.slug).first()
        return render(request, 'product/deleteProduct.html', locals())

    def post(self, request, *args, **kwargs):
        product = Product.objects.filter(slug=self.slug).first()
        if product.delete():
            return redirect(reverse("product:productview"))
        return render(request, 'product/deleteProduct.html', locals())

class UpdateProductView(View):
    
    def get(self, request, *args, **kwargs):
        
        return render(request, 'product/updateProduct.html', locals())

class SearchProductView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')
        products = Product.objects.filter(name__icontains=query)
        print(products)
        return render(request, 'product/searchProduct.html', locals())
