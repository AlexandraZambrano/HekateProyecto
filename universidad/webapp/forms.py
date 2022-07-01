from django.forms import ModelForm

from universidad.webapp.models import Profesor


class RegistroForm(ModelForm):
    class Meta:
        model = Profesor f