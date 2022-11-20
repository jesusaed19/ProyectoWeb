from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import FormUserLogin, FormUserRegister


# Create your views here.

class RegistroLogin(View):
    
    def get(self, request):
        
        form =FormUserRegister()
        return render(request, 'Login/registrate.html', {'form':form})
    
    def post(self, request):
        
        form=FormUserRegister(request.POST)
        
        if form.is_valid():
            
            usuario = form.save()
        
            login(request, usuario)
        
            return redirect('Panel')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
                
            return render(request, 'Login/registrate.html', {'form':form})
        
        
def cerrar_sesion(request):
    logout(request)
    
    return redirect('Signin')


def iniciar_sesion(request):
    
    formLogin = FormUserLogin()    
    
    if request.method=="POST":
        formLogin=FormUserLogin(request, data=request.POST)
        if formLogin.is_valid():
            nombre_usuario=formLogin.cleaned_data.get("username")
            password=formLogin.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario, password=password)
            if usuario is not None:
                login(request, usuario)
                return redirect('Panel')
            else:
                messages.error(request, 'Usuario no valido')
        else:
            messages.error(request, 'Informacion Incorrecta')  
            
    formLogin = FormUserLogin()
    return render(request, 'Login/login.html', {'form_login':formLogin})  
            
        
                
