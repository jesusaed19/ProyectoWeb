from django.contrib import admin
from .models import Cliente

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'direccion', 'email', 'tfn')
    search_fields = ('nombre', 'apellido')
    
admin.site.register(Cliente, ClienteAdmin)
