from django.contrib import admin
from core.erp.models import *

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Category)
admin.site.register(Sale)
admin.site.register(SaleDetail)


