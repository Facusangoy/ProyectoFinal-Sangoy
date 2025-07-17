from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models import Reserva, Comentario, AboutMe
from .forms import ReservaForm, ComentarioForm, RespuestaAdminForm, PerfilForm, AvatarForm
from datetime import date

# Inicio
def inicio(request):
    return render(request, 'bar/inicio.html')

# Carta
def carta(request):
    return render(request, 'bar/carta.html')

def desayunos_y_meriendas(request):
    return render(request, 'bar/Desayunos_y_Meriendas.html')

def almuerzo_y_cena(request):
    return render(request, 'bar/Almuerzo_y_Cena.html')

def bebidas(request):
    return render(request, 'bar/Bebidas.html')

def vinos_y_cocteles(request):
    return render(request, 'bar/Vinos_y_Cocteles.html')

# Reservar
@login_required(login_url='login')
def reservar_mesa(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.user = request.user
            reserva.save()
            messages.success(request, '¡Reserva confirmada exitosamente!')
            form = ReservaForm()
    else:
        form = ReservaForm()
    return render(request, 'bar/reserva_form.html', {'form': form})

@staff_member_required
def eliminar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    if request.method == 'POST':
        reserva.delete()
        messages.success(request, 'Reserva eliminada correctamente.')
    return redirect('panel_de_administracion')

# Comentarios
class ComentarioListView(ListView):
    model = Comentario
    template_name = 'bar/comentario_list.html'
    context_object_name = 'comentarios'
    ordering = ['-creado']

class ComentarioCreateView(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = 'bar/comentario_form.html'
    success_url = reverse_lazy('comentarios')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class ComentarioUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = 'bar/comentario_form.html'
    success_url = reverse_lazy('comentarios')

    def test_func(self):
        comentario = self.get_object()
        return self.request.user == comentario.usuario or self.request.user.is_superuser

class ComentarioDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comentario
    template_name = 'bar/comentario_confirm_delete.html'
    success_url = reverse_lazy('comentarios')

    def test_func(self):
        comentario = self.get_object()
        return self.request.user == comentario.usuario or self.request.user.is_superuser

@staff_member_required
def responder_comentario(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    if request.method == 'POST':
        form = RespuestaAdminForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect('comentarios')
    else:
        form = RespuestaAdminForm(instance=comentario)
    return render(request, 'bar/responder_comentario.html', {'form': form, 'comentario': comentario})

# Panel de admin 
@staff_member_required
def admin_dashboard(request):
    usuario_busqueda = request.GET.get('usuario', '').strip()
    buscar_usuario = request.GET.get('buscar_usuario', '').strip()
    Reserva.objects.filter(fecha__lt=date.today()).delete()

    reservas = Reserva.objects.all()
    if usuario_busqueda:
        reservas = reservas.filter(nombre__icontains=usuario_busqueda)
    reservas = reservas.order_by('fecha', 'hora')

    usuarios = User.objects.all()
    if buscar_usuario:
        usuarios = usuarios.filter(username__icontains=buscar_usuario)

    context = {
        'reservas': reservas,
        'usuario_busqueda': usuario_busqueda,
        'usuarios': usuarios,
        'buscar_usuario': buscar_usuario,
    }
    return render(request, 'bar/panel_de_administracion.html', context)

def admin_required(view_func):
    return user_passes_test(lambda u: u.is_superuser)(view_func)

# CRUD admin sobre comentarios
@staff_member_required
def editar_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id)

    if request.method == 'POST':
        comentario_form = ComentarioForm(request.POST, instance=comentario)
        respuesta_form = RespuestaAdminForm(request.POST, instance=comentario)
        if comentario_form.is_valid() and respuesta_form.is_valid():
            comentario_form.save()
            respuesta_form.save()
            return redirect('comentarios')
    else:
        comentario_form = ComentarioForm(instance=comentario)
        respuesta_form = RespuestaAdminForm(instance=comentario)

    context = {
        'comentario_form': comentario_form,
        'respuesta_form': respuesta_form,
        'comentario': comentario,
    }
    return render(request, 'bar/editar_comentario.html', context)

@staff_member_required
def borrar_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id)
    if request.method == 'POST':
        comentario.delete()
        return redirect('comentarios')
    return render(request, 'bar/confirmar_borrado.html', {'comentario': comentario})

# About
def about(request):
    aboutme = AboutMe.objects.first()
    return render(request, 'bar/about.html', {'aboutme': aboutme})

# Ubicación
def ubicacion(request):
    lat = -34.6037
    lon = -58.3816
    return render(request, 'bar/ubicacion.html', {'lat': lat, 'lon': lon})

@staff_member_required
def editar_perfil_admin(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        form = PerfilForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil actualizado con éxito.")
            return redirect('panel_de_administracion')
    else:
        form = PerfilForm(instance=user)
    return render(request, 'bar/editar_perfil_admin.html', {'form': form, 'user': user})

# Staff acciones
@staff_member_required
def editar_avatar_admin(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    perfil = user.perfil 
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            messages.success(request, "Avatar actualizado con éxito.")
            return redirect('panel_de_administracion')
    else:
        form = AvatarForm(instance=perfil)
    return render(request, 'bar/editar_avatar_admin.html', {'form': form, 'user': user})

@staff_member_required
def eliminar_usuario(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        user.delete()
        messages.success(request, "Usuario eliminado correctamente.")
        return redirect('panel_de_administracion')
    return render(request, 'bar/confirmar_eliminar_usuario.html', {'user': user})

# Favicon
def subir_favicon(request):
    if request.method == 'POST' and request.FILES.get('favicon'):
        favicon = request.FILES['favicon']
        fs = FileSystemStorage(location=settings.MEDIA_ROOT)
        
        filename = fs.save('faviconn.ico', favicon)
        return redirect('inicio')  

    return render(request, 'bar/favicon_upload.html')