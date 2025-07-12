from django.shortcuts import render

def inicio(request):
    return render(request, 'bar/inicio.html')

def about(request):
    return render(request, 'bar/about.html')

def carta(request):
    return render(request, 'bar/carta.html')

def ubicacion(request):
    return render(request, 'bar/ubicacion.html')

def opiniones_list(request):
    return render(request, 'bar/opiniones.html')

def reservas_list(request):
    return render(request, 'bar/reservas.html')
