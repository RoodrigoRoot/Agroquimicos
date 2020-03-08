from django.contrib import admin
from .models import *
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    class Meta:
        model = Product
    fields = ("name", "user", "description", "category",)
    list_display = ["name", "slug", "category","created_at", "modified_at"]
    search_fields = ["name", "category__name"]

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)

class DetailProductAdmin(admin.ModelAdmin):
    class Meta:
        model = DetailProduct
    list_display = ["product", "expiration", "price", "created_at", "modified_at" ]

admin.site.register(DetailProduct, DetailProductAdmin)

class WarehouseAdmin(admin.ModelAdmin):

    class Meta:
        model = Warehouse
    list_display = ["product", "user", "quantity", "created_at", "modified_at"]
    search_fields = ["product__name", "user__username"]
admin.site.register(Warehouse, WarehouseAdmin)