from django import forms
from django.contrib.auth.models import User
from .models import Reserva, Comentario, AboutMe, Perfil

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['nombre', 'email', 'fecha', 'hora', 'telefono', 'cantidad_personas']
        labels = {
            'cantidad_personas': 'Personas',
            'telefono': 'Teléfono',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'fecha': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Selecciona una fecha',
                'id': 'id_fecha'
            }),
            'hora': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Selecciona una hora',
                'id': 'id_hora'
            }),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu teléfono'}),
            'cantidad_personas': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Escribe tu comentario aquí...'}),
        }

class RespuestaAdminForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['respuesta_admin']
        widgets = {
            'respuesta_admin': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
        }

class AboutMeForm(forms.ModelForm):
    class Meta:
        model = AboutMe
        fields = ['photo', 'description']
        labels = {
            'photo': 'Foto',
            'description': 'Descripción',
        }

class PerfilForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Perfil 
        fields = ['avatar']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

class RegistroForm(forms.ModelForm):
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("El nombre de usuario ya existe.")
        return username

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password and password2 and password != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
