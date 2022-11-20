from django.urls import path

from .views import RegistroLogin

urlpatterns = [
    path('', RegistroLogin.as_view, name="Autenticacion"),
]
