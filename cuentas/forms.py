from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class RegistroUsuarioForm(UserCreationForm):
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField(label="Correo electrónico")
    dni = forms.CharField(label="DNI")
    telefono = forms.CharField(label="Teléfono")
    avatar = forms.ImageField(required=False, label="Avatar (opcional)")

    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name', 'email',
            'dni', 'telefono', 'avatar', 'password1', 'password2'
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
            profile, created = Profile.objects.get_or_create(user=user)
            profile.dni = self.cleaned_data['dni']
            profile.telefono = self.cleaned_data['telefono']
            avatar = self.cleaned_data.get('avatar')
            if avatar:
                profile.avatar = avatar
            profile.save()

        return user

class PasswordChangeByUserInfoForm(forms.Form):
    username = forms.CharField(max_length=150, label="Nombre de usuario")
    dni = forms.CharField(max_length=20, label="DNI")
    telefono = forms.CharField(max_length=20, label="Teléfono")
    new_password1 = forms.CharField(widget=forms.PasswordInput, label="Nueva contraseña")
    new_password2 = forms.CharField(widget=forms.PasswordInput, label="Repetir nueva contraseña")

    def clean(self):
        cleaned_data = super().clean()
        pw1 = cleaned_data.get("new_password1")
        pw2 = cleaned_data.get("new_password2")

        if pw1 and pw2 and pw1 != pw2:
            raise forms.ValidationError("Las contraseñas no coinciden.")

        username = cleaned_data.get("username")
        dni = cleaned_data.get("dni")
        telefono = cleaned_data.get("telefono")

        if username and dni and telefono:
            try:
                user = User.objects.get(username=username)
                profile = user.profile
            except (User.DoesNotExist, Profile.DoesNotExist):
                raise forms.ValidationError("Usuario no encontrado.")

            if profile.dni != dni or profile.telefono != telefono:
                raise forms.ValidationError("DNI o teléfono incorrectos.")
        else:
            raise forms.ValidationError("Por favor completa todos los campos.")
        return cleaned_data

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']
        labels = {'avatar': 'Seleccioná tu imagen'}
