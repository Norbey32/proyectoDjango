from django.db import models
from datetime import datetime


class Type(models.Model):
        name = models.CharField(max_length=150, verbose_name="Nombre")

        def __str__(self):
            return self.name
        
        class Meta:
            verbose_name = "tipo"
            verbose_name_plural = "tipos"
            db_table = "Tipo"
            ordering = ['id']


class Category(models.Model):
        name = models.CharField(max_length=150, verbose_name="Nombre")

        def __str__(self):
            return self.name

        class Meta:
            verbose_name = "categoría"
            verbose_name_plural = "categorías"
            db_table = "Categoria"
            ordering = ['id']



class Employee(models.Model):
    category = models.ManyToManyField(Category)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, verbose_name="Nombres")
    dni = models.CharField(max_length=10, unique=True, verbose_name="DNI")
    date_joined = models.DateField(default=datetime.now, verbose_name="Fecha de registro")
    date_creation = models.DateField(auto_now=True)
    date_modification = models.DateField(auto_now_add=True)
    age = models.PositiveBigIntegerField(default=0)
    salary = models.DecimalField(max_digits=9, decimal_places=2)
    state = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)
    cvitae = models.FileField(upload_to='cvitae/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "empleado"
        verbose_name_plural = "empleados"
        db_table = "Empleado"
        ordering = ['id']