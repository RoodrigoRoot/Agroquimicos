from django.urls import path
from .views import *

urlpatterns = [
    path("", ProductView.as_view(), name="productview"),
    path("eliminar/<slug:slug>/", DeleteProductView.as_view(), name="deleteproduct"),
    path("actualizar/<slug:slug>/", UpdateProductView.as_view(), name="updateproduct"),
    path("agregar/", AddProductView.as_view(), name="addproduct"),
    path("search", SearchProductView.as_view(), name="searchproduct"),
]
