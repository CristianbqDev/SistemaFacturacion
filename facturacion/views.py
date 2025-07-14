from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ProductoForm
from .forms import FacturaForm
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


from .forms import FacturaForm

def crear_factura(request):
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_factura')
    else:
        form = FacturaForm()
    
    return render(request, 'crear_factura.html', {'form': form})

