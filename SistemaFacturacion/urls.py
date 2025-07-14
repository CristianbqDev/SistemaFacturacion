from django.urls import path
from facturacion.views import crear_producto
from facturacion.views import crear_factura
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', crear_producto),  # Ruta raíz
    path('crear-producto/', crear_producto, name='crear_producto'),
     path('crear-factura/', crear_factura, name='crear_factura'),
]
