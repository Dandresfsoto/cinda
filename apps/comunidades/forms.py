from django import forms
from .models import ComunidadEntry
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Fieldset, Row, Column, Layout, Submit, ButtonHolder

class ComunidadEntryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ComunidadEntryForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_id = "id_form"
        self.helper.layout = Layout(
            Row(
                Column(
                    'nombre',
                    css_class="form-group col-lg-12 mt-2"
                ),
                Column(
                    'photo',
                    css_class="form-group col-lg-12"
                ),
                Column(
                    'markdown',
                    css_class="form-group hide col-lg-12"
                ),
                Column(
                    'descripcion',
                    css_class="form-group col-lg-12"
                ),
            ),
            ButtonHolder(
                Submit(
                    'submit',
                    'Guardar',
                    css_class='btn btn-success mt-2'
                )
            )
        )

    class Meta:
        model = ComunidadEntry
        fields = ['nombre', 'photo', 'markdown', 'descripcion']
        labels = {
            'photo': 'Imagen'
        }
