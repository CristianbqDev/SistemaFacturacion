from django.urls import path, include
from . import views

urlpatterns = [
    path('facturas/', views.listar_facturas, name='listar_facturas'),
    path('crear-factura/', views.crear_factura, name='crear_factura'),
    path('editar-factura/<int:factura_id>/', views.editar_factura, name='editar_factura'),
    path('eliminar-factura/<int:factura_id>/', views.eliminar_factura, name='eliminar_factura'),
]
