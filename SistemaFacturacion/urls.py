from django.contrib import admin
from django.urls import path
from facturacion.views import inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
]
