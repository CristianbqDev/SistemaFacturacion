from django.contrib import admin
from django.urls import path, include
from facturacion.views import crear_producto
from facturacion.views import crear_factura
from facturacion.views import listar_productos
from facturacion.views import eliminar_producto
from facturacion.views import editar_producto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('facturacion.urls')),
    path('', crear_producto),  # Ruta raíz
    path('crear-producto/', crear_producto, name='crear_producto'),
    path('productos/', listar_productos, name='listar_productos'),
    path('eliminar-producto/<int:producto_id>/', eliminar_producto, name='eliminar_producto'),
    path('editar-producto/<int:producto_id>/', editar_producto, name='editar_producto'),
    

]

