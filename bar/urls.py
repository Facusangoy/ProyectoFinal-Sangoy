from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('about/', views.about, name='about'),
    path('carta/', views.carta, name='carta'),
    path('ubicacion/', views.ubicacion, name='ubicacion'),
    path('opiniones/', views.opiniones_list, name='opiniones'),
    path('reservas/', views.reservas_list, name='reservas'),
]
