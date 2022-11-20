from django.shortcuts import render, redirect
from .models import Productos
from .forms import ProductosForm
from django.views.generic import View

# Create your views here.


class ModalProductos(View):
    
    def get(self, request):
        form = ProductosForm()
        productos = Productos.objects.all()
        return render(request, "Productos/productos.html", {'productos':productos, 'form':form})
    
    def post(self, request):
        form = ProductosForm(request.POST)
        productos = Productos.objects.all()
        
        if form.is_valid():
            
            form.save()
            
            return redirect('Productos')
            
        # return render(request, "Productos/productos.html", {'productos':productos, 'form':form})
        
            
            
        
    

    
