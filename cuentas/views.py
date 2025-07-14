from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import (
    RegistroUsuarioForm,
    PasswordChangeByUserInfoForm,
    AvatarForm
)
from .models import Profile

def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('login'))
    else:
        form = RegistroUsuarioForm()
    return render(request, 'cuentas/crear_cuenta.html', {'form': form})


# Vista del perfil
@login_required
def perfil_view(request):
    perfil = request.user.profile
    return render(request, 'cuentas/perfil.html', {
        'user': request.user,
        'perfil': perfil
    })


@login_required
def ver_perfil(request):
    perfil = Profile.objects.get(user=request.user)
    return render(request, 'cuentas/perfil.html', {'perfil': perfil})

def cambiar_password_por_info_usuario(request):
    if request.method == "POST":
        form = PasswordChangeByUserInfoForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            new_password = form.cleaned_data['new_password1']
            user = User.objects.get(username=username)
            user.set_password(new_password)
            user.save()
            messages.success(request, "Contraseña cambiada correctamente.")
            return redirect('login')
    else:
        form = PasswordChangeByUserInfoForm()

    return render(request, 'cuentas/cambiar_contraseña.html', {'form': form})

@login_required
def subir_avatar(request):
    perfil = request.user.profile

    if perfil.avatar:
        messages.info(request, "Ya tenés un avatar.")
        return redirect('ver_perfil')  

    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            messages.success(request, "Avatar subido correctamente.")
            return redirect('ver_perfil') 
    else:
        form = AvatarForm()

    return render(request, 'cuentas/subir_avatar.html', {'form': form})