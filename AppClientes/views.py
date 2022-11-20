from django.shortcuts import render

from .models import Cliente

# Create your views here.



def Clientes(request):
    
    clientes = Cliente.objects.all()
    
    return render(request, "AppClientes/clientes.html", {"clientes":clientes})