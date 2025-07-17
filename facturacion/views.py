from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ProductoForm
from .forms import FacturaForm
from .models import Producto
from .models import Factura
from django.shortcuts import render, get_object_or_404, redirect
import datetime


def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_producto')
    else:
        form = ProductoForm()
    
    return render(request, 'crear_producto.html', {'form': form})

def crear_factura(request):
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_factura')
    else:
        form = FacturaForm()
    
    return render(request, 'crear_factura.html', {'form': form})

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listar_productos.html', {'productos': productos})

def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.delete()
    return redirect('listar_productos')

def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')      
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'editar_producto.html', {'form': form, 'producto': producto})


#Facturación:

def listar_facturas(request):
    facturas = Factura.objects.all()
    return render(request, 'listar_facturas.html', {'facturas': facturas})

def crear_factura(request):
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_facturas')
    else:
        form = FacturaForm()

    return render(request, 'crear_factura.html', {'form': form})

def editar_factura(request, factura_id):
    factura = get_object_or_404(Factura, id=factura_id)
    if request.method == 'POST':
        form = FacturaForm(request.POST, instance=factura)
        if form.is_valid():
            form.save()
            return redirect('listar_facturas')
    else:
        form = FacturaForm(instance=factura)
    return render(request, 'editar_factura.html', {'form': form})

def eliminar_factura (request,factura_id):
    factura = get_object_or_404(Factura, id=factura_id)
    factura.delete()
    return redirect('listar_facturas')



