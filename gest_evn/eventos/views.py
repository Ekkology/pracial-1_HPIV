from django.shortcuts import render
from  .forms  import EventoForm

def lista_home(request):
        form = EventoForm()
        return render(request,"lista_eventos.html",{"form": form})
