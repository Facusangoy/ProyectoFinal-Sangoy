from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='avatares/', blank=True, null=True)
    dni = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    
    def __str__(self):
        return f'Perfil de {self.user.username}'
    
class AvatarDefault(models.Model):
    imagen = models.ImageField(upload_to='avatares/default/')
    
    def __str__(self):
        return "Avatar por defecto"
    
@receiver(post_save, sender=User)
def crear_o_actualizar_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)
    
    profile = instance.profile

    if not profile.avatar:
        try:
            avatar_default = AvatarDefault.objects.first()
            if avatar_default and avatar_default.imagen:
                profile.avatar = avatar_default.imagen
                profile.save()
        except AvatarDefault.DoesNotExist:
            pass