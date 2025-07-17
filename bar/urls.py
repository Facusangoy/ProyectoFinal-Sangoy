from django.urls import path
from . import views
from .views import (
    inicio, carta, reservar_mesa, about, ubicacion,
    ComentarioListView, ComentarioCreateView,
    ComentarioUpdateView, ComentarioDeleteView,
    eliminar_reserva
)
from .views import subir_favicon

urlpatterns = [
    path('', inicio, name='inicio'),
    path('carta/', carta, name='carta'),
    path('carta/desayunos/', views.desayunos_y_meriendas, name='desayunos_y_meriendas'),
    path('carta/almuerzo/', views.almuerzo_y_cena, name='almuerzo_y_cena'),
    path('carta/bebidas/', views.bebidas, name='bebidas'),
    path('carta/vinos/', views.vinos_y_cocteles, name='vinos_y_cocteles'),
    path('reservar/', reservar_mesa, name='reserva'),
    path('about/', about, name='about'),
    path('ubicacion/', ubicacion, name='ubicacion'),
    path('comentarios/', ComentarioListView.as_view(), name='comentarios'),
    path('comentarios/nuevo/', ComentarioCreateView.as_view(), name='crear_comentario'),
    path('comentarios/<int:pk>/editar/', ComentarioUpdateView.as_view(), name='editar_comentario'),
    path('comentarios/<int:pk>/eliminar/', ComentarioDeleteView.as_view(), name='eliminar_comentario'),
    path('comentarios/<int:pk>/responder/', views.responder_comentario, name='responder_comentario'),
    path('admin/dashboard/', views.admin_dashboard, name='panel_de_administracion'),
    path('admin/reservas/<int:reserva_id>/eliminar/', eliminar_reserva, name='eliminar_reserva'),
    path('editar_perfil_admin/<int:user_id>/', views.editar_perfil_admin, name='editar_perfil_admin'),
    path('eliminar_usuario/<int:user_id>/', views.eliminar_usuario, name='eliminar_usuario'),
]