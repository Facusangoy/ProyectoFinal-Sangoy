from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('carta/', views.carta, name='carta'),
    path('reservar/', views.reservar_mesa, name='reserva'),
    path('comentario/nuevo/', views.dejar_comentario, name='comentario'),
    path('comentarios/', views.ver_comentarios, name='comentarios'),
    path('ubicacion/', views.ubicacion, name='ubicacion'),
]