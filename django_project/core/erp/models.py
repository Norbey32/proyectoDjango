from django.db import models
from datetime import datetime

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    dni = models.CharField(max_length=10, unique=True)
    date_birth = models.DateField()
    direccion = models.CharField(max_length=255)
    sex = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Femenino')])

    def __str__(self):
        return f"{self.name} {self.last_name}"
    
    class Meta:
       verbose_name = "cliente"
       verbose_name_plural = "clientes"
       db_table = "Cliente"
       ordering = ['id']

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='productos/%Y/%m/%d', null=True, blank=True)
    pvp = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"
        db_table = "Producto"
        ordering = ['id']

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "categorías"
        db_table = "Categoria"
        ordering = ['id']


class Sale(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    date_sale = models.DateTimeField(default=datetime.now)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    iva = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Venta {self.id} - {self.cliente.name}"
    
    class Meta:
        verbose_name = "venta"
        verbose_name_plural = "ventas"
        db_table = "Venta"
        ordering = ['id']

class SaleDetail(models.Model):
    id = models.AutoField(primary_key=True)
    venta = models.ForeignKey(Sale, related_name='details', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Detalle de Venta {self.id} - {self.producto.name}"
    
    class Meta:
        verbose_name = "detalle de venta"
        verbose_name_plural = "detalles de venta"
        db_table = "Detalle_Venta"
        ordering = ['id']