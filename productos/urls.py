from django.urls import path

from .views import ModalProductos
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('', ModalProductos.as_view(), name="Productos"),
    
]


