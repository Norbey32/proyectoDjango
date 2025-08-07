from django.db import models
from datetime import datetime

class Empleado(models.Model):
    name = models.CharField(max_length=150, verbose_name="Nombres")
    dni = models.CharField(max_length=10, unique=True, verbose_name="DNI")
    date_joined = models.DateField(default=datetime.now, verbose_name="Fecha de registro")
    date_create = models.DateField(auto_now=True,)
    


