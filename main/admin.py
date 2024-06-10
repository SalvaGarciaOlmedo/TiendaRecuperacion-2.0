from django.contrib import admin
from django.contrib.auth.models import User

from main.models import *
from shop.models import Marca, Producto, Compra, Valoracion, ItemCarrito

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Tarjeta)
admin.site.register(Direccion)
admin.site.register(Marca)
admin.site.register(Producto)
admin.site.register(Compra)
admin.site.register(ItemCarrito)
admin.site.register(Valoracion)