from .models import Dvigateli
from django.forms import ModelForm, TextInput, Select, CheckboxInput

class DvigateliForm(ModelForm):
    class Meta:
        model = Dvigateli
        fields = ['model', 'vid_eto', 'tip_1', 'tip_2', 'tip_3', 'napr', 'chast']

        widgets = {
            "model": TextInput(attrs={
                # "class": 'form-control',
                "id": 'mod',
                'placeholder': 'Введите модель...'
            }),
            "vid_eto": Select(attrs={
                'class': 'select-css',
                'id': 'vid',
            }),
            "tip_1": CheckboxInput(attrs={
                'class': 'form-check-input',
                'id': 'osnov'
            }),
            "tip_2": CheckboxInput(attrs={
                'class': 'form-check-input',
                'id': 'dop'
            }),
            "tip_3": CheckboxInput(attrs={
                'class': 'form-check-input',
                'id': 'vspomog'
            }),
            "napr": TextInput(attrs={
                # 'class': 'form-check-input',
                'id': 'napr',
                'placeholder': 'Введите напряжение...'
            }),
            "chast": TextInput(attrs={
                # 'class': 'form-check-input',
                'id': 'chast',
                'placeholder': 'Введите частоту...'
            })
        }