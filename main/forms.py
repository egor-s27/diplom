from .models import Znaniya
from django.forms import ModelForm, TextInput, Select, NumberInput

class ZnaniyaForm(ModelForm):
    class Meta:
        model = Znaniya
        fields = ['vid_eto', 'vid_metod', 'otl_koleb', 'nes', 'sin', 'otl_chast', 'pomehi']

        widgets = {
            "vid_eto": Select(attrs={
                # 'class': 'form-control',
                'id': 'vid'
            }),
            "vid_metod": Select(attrs={
                # 'class': 'form-control',
                'id': 'vid_m'
            }),
            "otl_koleb": NumberInput(attrs={
                'class': 'form',
                'placeholder': 'Отклонение и колебание напряжния',
                'min': '0',
                'max': '1',
                'step': '0.1'
            }),
            "nes": NumberInput(attrs={
                # 'class': 'form-control',
                'placeholder': 'Нессиметрия напряжния',
                'min': '0',
                'max': '1',
                'step': '0.1'

            }),
            "sin": NumberInput(attrs={
                # 'class': 'form-control',
                'placeholder': 'Синусоидальность напряжния',
                'min': '0',
                'max': '1',
                'step': '0.1'
            }),
            "otl_chast": NumberInput(attrs={
                # 'class': 'form-control',
                'placeholder': 'Отклонение частоты',
                'min': '0',
                'max': '1',
                'step': '0.1'
            }),
            "pomehi": NumberInput(attrs={
                # 'class': 'form-control',
                'placeholder': 'Электромагнитные помехи',
                'min': '0',
                'max': '1',
                'step': '0.1'
            })
        }
