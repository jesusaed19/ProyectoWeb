from importlib import import_module
from django.contrib import admin

# Register your models here.


from .models import  Productos

    
    
# class CategoriaAdmin(admin.ModelAdmin):
#     list_display = ('titulo', 'imagen')
    
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('producto', 'marca', 'seccion', 'cantidad', 'precio')
    search_fields = ('producto', 'marca', 'seccion')

admin.site.register(Productos, ProductoAdmin)

# admin.site.register(Categoria, CategoriaAdmin)