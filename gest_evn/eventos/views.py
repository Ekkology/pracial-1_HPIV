from django.shortcuts import render
from  .forms  import EventoForm
from  .models import Organizador
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Organizador
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Evento
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class OrganizadorListView(ListView):
    model = Organizador
    template_name = 'organizadores_listar.html'
    context_object_name = 'organizadores'

class OrganizadorCreateView(CreateView):
    model = Organizador
    template_name = 'organizadores_crear.html'
    fields = ['nombre']
    success_url = reverse_lazy('organizador-list')



def listar_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'listar_eventos.html', {'eventos': eventos})





from django.shortcuts import render, redirect
from .forms import EventoForm

def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('listar_eventos')  
    else:
        form = EventoForm()
    return render(request, "crear_eventos.html", {"form": form})



@login_required
def editar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('listar_eventos')  # Redirige a la lista de eventos después de guardar cambios
    else:
        form = EventoForm(instance=evento)
    return render(request, 'editar_eventos.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Autenticar automáticamente al usuario después del registro
            return redirect('eventos')  # Redirige a la página que prefieras después del registro
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
