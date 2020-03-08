from django.contrib import admin
from django.urls import path, include
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Core.urls')),
    path('Productos/', include(("Products.urls", 'product'))),
    path('__debug__/', include(debug_toolbar.urls)),
]
