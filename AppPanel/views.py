from django.shortcuts import render, HttpResponse

from AppClientes.models import Cliente

# Create your views here.

def index(request):
    clientes = Cliente.objects.all()
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:            
            return render(request, "AppPanel/panel.html", {"clientes":clientes})
        
        else:
            return HttpResponse('Login')
    
    


