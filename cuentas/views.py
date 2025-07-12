from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from .models import Perfil
from .forms import ProfileUpdateForm

@login_required
def perfil_view(request):
    perfil_usuario = request.user.perfil
    return render(request, 'cuentas/perfil.html', {'perfil': perfil_usuario, 'user': request.user})

def crear_cuenta(request):
    return render(request, 'cuentas/crear_cuenta.html')

@login_required
def editarPerfil(request):
    perfil_usuario = request.user.perfil
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=perfil_usuario)
        if form.is_valid():     
            form.save()
            return redirect('perfil')
    else:
        form = ProfileUpdateForm(instance=perfil_usuario)

    return render(request, 'cuentas/editarPerfil.html', {'form': form})


@login_required
def cambiar_contraseña(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('perfil')
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'cuentas/cambiar_contraseña.html', {'form': form})
