from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile, AvatarDefault

@receiver(post_save, sender=User)
def crear_o_actualizar_profile(sender, instance, created, **kwargs):
    profile, created_profile = Profile.objects.get_or_create(user=instance)
    if not profile.avatar:
        try:
            avatar_default = AvatarDefault.objects.first()
            if avatar_default and avatar_default.imagen:
                profile.avatar = avatar_default.imagen
                profile.save()
        except AvatarDefault.DoesNotExist:
            pass
