from django.urls import path
from .views import lista_home

urlpatterns = [
    path('eventos/', lista_home , name='lista_eventos'),
]

