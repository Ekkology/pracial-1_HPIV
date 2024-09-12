from django.urls import path
from .views import OrganizadorListView, OrganizadorCreateView
from . import views

urlpatterns = [
    path('eventos/', views.listar_eventos, name='listar_eventos'),
    path('eventos/crear/', views.crear_evento, name='crear_evento'),
    path('eventos/editar/<int:pk>/', views.editar_evento, name='editar_evento'),
    path('organizadores/', OrganizadorListView.as_view(), name='organizador-list'),
    path('organizadores/nuevo/', OrganizadorCreateView.as_view(), name='organizador-create'),
]

