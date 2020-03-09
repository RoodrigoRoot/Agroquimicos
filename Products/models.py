from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import pre_save

# Create your models here.
    
class Category(models.Model):
                              
    CATEGORY = [
        ("Liquido","Liquido"),
        ("Polvo", "Polvo")
        ]

    name = models.CharField(("Nombre"), max_length=100, choices=CATEGORY)
    description = models.TextField(("Descripción"), null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(("Producto"), max_length=100, blank=False, null=False)
    description = models.TextField(("Descripción"), blank=True, null=True)
    category = models.ForeignKey(Category, verbose_name=("Categoria"), on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(User, verbose_name=("Usuario"), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
    
    def __str__(self):
        return self.name

def create_slug_product(sender, instance, *args, **kwargs):
    instance.slug = slugify("{}-{}".format(instance.name, instance.category))

pre_save.connect(create_slug_product, sender=Product)

class DetailProduct(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    expiration = models.DateField(("Expiración"), auto_now=False, auto_now_add=False)
    price = models.FloatField(("Precio"))
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    user = models.ForeignKey(User, verbose_name=("Usuario"), on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Detalle del Producto"
        verbose_name_plural = "Detalles del Producto"
    
    def __str__(self):
        return "Detalles de {}".format(self.product)
    

class Warehouse(models.Model):
    product = models.OneToOneField( Product, on_delete=models.CASCADE)
    user = models.ForeignKey( User, on_delete=models.CASCADE)
    quantity = models.IntegerField(("Cantidad"), default=0, blank=False, null=False)
    user = models.ForeignKey(User, verbose_name=("Usuario"), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = "Almacen"
        verbose_name_plural = "Almacen"
    
    def __str__(self):
        return "{} : {}".format(self.product, self.quantity)