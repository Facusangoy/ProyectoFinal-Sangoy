from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Plato, Comentario
from .forms import ReservaForm, ComentarioForm

def inicio(request):
    return render(request, 'bar/inicio.html')
    
def carta(request):
    platos = Plato.objects.all()
    return render(request, 'bar/carta.html', {'platos': platos})

@login_required(login_url='login') 
def reservar_mesa(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.user = request.user
            reserva.save()
            return redirect('reserva_exitosa') 
    else:
        form = ReservaForm()
    return render(request, 'bar/reserva_form.html', {'form': form})

@login_required
def dejar_comentario(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.save()
            return redirect('ver_comentarios')
    else:
        form = ComentarioForm()
    return render(request, 'bar/comentario_form.html', {'form': form})

def ver_comentarios(request):
    comentarios = Comentario.objects.all().order_by('-creado')
    return render(request, 'bar/comentario_list.html', {'comentarios': comentarios})

def ubicacion(request):
    return render(request, 'bar/ubicacion.html')