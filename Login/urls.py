from django.urls import path

from .views import RegistroLogin, cerrar_sesion, iniciar_sesion

urlpatterns = [
    path('registrate/', RegistroLogin.as_view(), name= "Login"),
    path('cerrar_sesion/', cerrar_sesion, name= "Logout"),
    path('login/', iniciar_sesion, name= "Signin"),
]
