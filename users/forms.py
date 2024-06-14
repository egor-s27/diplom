from .models import User
from django.forms import ModelForm, TextInput, PasswordInput, NumberInput

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['surname', 'name', 'mid_name', 'phone', 'login', 'pas']

        widgets = {
            "surname": TextInput(attrs={
                'placeholder': 'Иванов'
            }),
            "name": TextInput(attrs={
                'placeholder': 'Иван'
            }),
            "mid_name": TextInput(attrs={
                'placeholder': 'Иванович'
            }),
            "phone": TextInput(attrs={
                'placeholder': '89270665522'
            }),
            "login": TextInput(attrs={
                "class": 'form-control',
                "id": 'floatingInput',
                "placeholder": 'Логин'
            }),
            "pas": PasswordInput(attrs={
                "class": 'form-control',
                "id": 'floatingPassword',
                "placeholder": 'Пароль'
            }),
        }