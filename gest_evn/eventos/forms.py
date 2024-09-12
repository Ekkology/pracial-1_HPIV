from django.forms import ModelForm
from .models import Evento
from django import forms



class EventoForm(ModelForm):
     class Meta:
        model = Evento
        fields = ["nombre","Organizador","fecha"]
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'})  # Usa el widget de entrada de fecha
        }



form = EventoForm()