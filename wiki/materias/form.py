from django.forms import ModelForm
from .models import Materia


class MateriaForm(ModelForm):
    class Meta:
        model = Materia
        fields = ['titulo', 'categoria', 'subtitulo', 'texto']

    def __init__(self, *args, **kwargs):
        super(MateriaForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })
