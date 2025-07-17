from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import cambiar_password_por_info_usuario

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='cuentas/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='inicio'), name='logout'),
    path('signup/', views.registro, name='signup'),
    path('perfil/', views.perfil, name='perfil'),
    path('cambiar_contraseña/', cambiar_password_por_info_usuario, name='cambiar_contraseña'),
 ]
