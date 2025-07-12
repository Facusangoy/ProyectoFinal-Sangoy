from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='cuentas/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('crear/', views.crear_cuenta, name='crear_cuenta'),
    path('perfil/', views.Perfil, name='perfil'),
    path('perfil/editar/', views.editarPerfil, name='editar_perfil'),
    path('perfil/contraseña/', views.cambiar_contraseña, name='cambiar_contraseña'),
]
