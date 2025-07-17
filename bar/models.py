from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Plato(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)

class Reserva(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    fecha = models.DateField()
    hora = models.TimeField()
    telefono = models.CharField(max_length=20)
    cantidad_personas = models.PositiveIntegerField()

def __str__(self):
    user = self.usuario.username if self.usuario else "Anónimo"
    return f"Reserva de {user} el {self.fecha} a las {self.hora}"

class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)
    respuesta_admin = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Comentario de {self.usuario.username} el {self.creado}"

class AboutMe(models.Model):
    photo = models.ImageField(upload_to='about_photo/')
    description = models.TextField()

    def __str__(self):
        return "About Me"

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    avatar = models.ImageField(upload_to='avatares/', blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"

@receiver(post_save, sender=User)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)

@receiver(post_save, sender=User)
def guardar_perfil_usuario(sender, instance, **kwargs):
    try:
        perfil = instance.perfil
    except Perfil.DoesNotExist:
        perfil = Perfil.objects.create(user=instance)
    perfil.save()
