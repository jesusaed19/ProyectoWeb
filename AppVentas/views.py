from django.shortcuts import render

# Create your views here.

def ventas(request):
    
    return render(request, "AppVentas/ventas.html")