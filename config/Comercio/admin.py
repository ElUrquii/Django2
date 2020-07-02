from django.contrib import admin
from .models import *

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['rut', 'nombre', 'telefono']
    list_display_links = ['rut', 'nombre', 'telefono']

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    fieldsets = (
        ('Descripcion', {
            'fields':('categoria','nombre', 'proveedor',)
        }),
        ('Variables', {
            'fields':('precio','stock',)
        }),
    )

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'web']
    list_filter = ['nombre', 'rut']


admin.site.register(Categoria)
admin.site.register(Ciudad)
admin.site.register(Comuna)
admin.site.register(Direccion)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Venta)
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Detalle)
