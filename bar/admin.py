from django.contrib import admin
from .models import Plato, Reserva, Comentario

admin.site.register(Plato)
admin.site.register(Reserva)
admin.site.register(Comentario)