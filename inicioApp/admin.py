from django.contrib import admin
from .models import Usuario
from .models import Pedidos,tipopizza,formapago

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Pedidos)
admin.site.register(tipopizza)
admin.site.register(formapago)
