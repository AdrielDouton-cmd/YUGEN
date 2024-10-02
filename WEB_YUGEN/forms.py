from django import forms
from .models import Cliente, Evento, Reserva

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'telefono', 'email']

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre_evento', 'numero']

class ReservaForm(forms.ModelForm):
    class meta:
        model = Reserva
        fields = ['fecha', 'hora', 'numero_de_personas']