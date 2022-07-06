from django.forms import ModelForm, EmailInput

from webapp.models import *


class RegistroForm(ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type':'email'})
        }