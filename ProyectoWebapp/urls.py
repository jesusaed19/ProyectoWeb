from django.urls import path

from ProyectoWebapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', views.Login, name="Login"),
    # path('clientes/', views.Clientes, name="Clientes"),
    # path('compras/', views.Compras, name="Compras"),
    # path('ventas/', views.Ventas, name="Ventas"),
    # path('config/', views.Config, name="Config"),
    # path('dasboard/', views.index, name="Dasboard"),
    # path('panel/', views.Panel, name="Panel"),
    path('', views.modal, name="Modal"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
