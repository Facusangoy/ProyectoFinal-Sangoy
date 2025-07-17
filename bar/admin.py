from django.contrib import admin
from django.contrib.auth.models import User
from .models import Plato, Reserva, Comentario

admin.site.register(Plato)
admin.site.register(Reserva)

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'contenido', 'creado', 'respuesta_admin')
    list_filter = ('creado',)
    search_fields = ('usuario__username', 'contenido', 'respuesta_admin')
    ordering = ('-creado',)

admin.site.register(Comentario, ComentarioAdmin)
