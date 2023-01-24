from .models import Switches
from django.forms import ModelForm, TextInput

class SwitchesForm(ModelForm):
    class Meta:
        model = Switches
        fields = ['name', 'vendor', 'model', 'soft_version', 'serial_number', 'ip', 'location', 'buiding']
        
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название коммутатора'
            }),
            "vendor": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Производитель оборудования'
            }),
            "model": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Модель оборудования'
            }),
            "soft_version": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Версия прошивки'
            }),
            "serial_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Серийный номер'
            }),
            "ip": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'IP-адрес'
            }),
            "location": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Местонахождение'
            }),
            "buiding": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Здание'
            }),
        }