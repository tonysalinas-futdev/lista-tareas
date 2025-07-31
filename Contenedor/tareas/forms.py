from crispy_forms.helper import FormHelper
from crispy_forms. layout import Layout, Row, Column, Submit,Button, HTML, Div
from django.forms.widgets import DateInput
from django.utils import timezone
from django import forms 
from .models import Tarea


class TareaForm(forms.ModelForm):
    class Meta:
        model=Tarea
        fields=["nombre", "descripcion","fecha_vencimiento"]
        
        labels={"nombre":"Escriba el nombre de la tarea",
                "descripcion":"Escriba la descripcion de la tarea",
                "fecha_vencimiento":"Elija la fecha en la que desea que su tarea venza"}
        error_messages={
            "nombre":{"required":"Este campo es obligatorio",
                    "unique":"Ya existe una tarea con este nombre"}
        }
        help_text={"nombre":"Trate de no exceder los 255 caracteres"}


        widgets={"descripcion": forms.Textarea(attrs={
            "class": "form-control",
            "rows":4,
            "placeholder":"Descripcion de la tarea"
        }),
        "nombre":forms.TextInput(attrs={
            "class": "form-control",
            "placeholder":"Nombre de la tarea"
        }),
        "fecha_vencimiento":DateInput(attrs={
            "type": "date",
            "class": "form-control",
            "min": timezone.now().date().isoformat()
        })
        }

    # Nos aseguramos de que la fecha de vencimineto no sea anterior a la fecha de creacion de la tarea
    def clean_fecha_vencimiento(self):
        fecha = self.cleaned_data.get('fecha_vencimiento')
        if fecha:
            hoy = timezone.now().date()
            if fecha < hoy:
                raise forms.ValidationError("La fecha de vencimiento no puede ser en el pasado.")
        return fecha
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Row(
                Column('nombre', css_class='col-md-4'),
                Column('fecha_vencimiento', css_class='col-md-4'),
                css_class='g-3'
            ),
            'descripcion',
            Submit('submit', 'Crear tarea', css_class='btn btn-primary mt-3'),
        )
