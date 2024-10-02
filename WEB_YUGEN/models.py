from django.db import models

class Evento(models.Model):
    nombre_evento = models.CharField(max_length=50)
    numero = models.IntegerField()

    def __str__(self):
        return f'Evento: {self.nombre_evento}'

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Reserva(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    numero_de_personas = models.PositiveIntegerField()

    def __str__(self):
        return f"Reserva para la fecha: {self.fecha} ({self.hora})"