from django.shortcuts import render


def lista_home(request):
        return render(request,"lista_eventos.html")
