from contextlib import redirect_stderr
from pyexpat.errors import messages
from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.forms import AuthenticationForm

# Create your views here.


def modal(request):
    
    return render(request, "ProyectoWebapp/modal.html")



def Compras(request):
    
    return render(request, "Vistas/compras.html")


def Ventas(request):
    
    return render(request, "Vistas/ventas.html")



def Config(request):
    
    return render(request, "Vistas/config.html")



    
    

# def buscar(request):
    
#     if request.GET['bprd']:
#         # mensaje = 'Articulo buscado: %r' %request.GET['prd']
#         producto = request.GET['bprd']
        
#         if len(producto)>20:
            
#             mensaje = 'Texto de busqueda demasiado largo'
            
#         else:        
#             articulos = Productos.objects.filter(producto__icontains=producto)
#         # LA FUNCION ICONTAINS FUNCIONA COMOM UN LIKE DE SQL 
#             return render(request, 'Vistas/buscar.html', {"articulos":articulos})
        
#     else:
        
#         mensaje= 'No has introducido nada'
    

