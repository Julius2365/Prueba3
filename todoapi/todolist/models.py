from django.db import models

class Item(models.Model):
    nombre = models.CharField(max_length=255)  # Campo para el nombre del item
    descripcion = models.TextField()  # Campo para la descripción del item
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Campo para el precio del item

    def __str__(self):
        return self.nombre  # Representación en cadena del objeto, muestra el nombre del item en la administración de Django

