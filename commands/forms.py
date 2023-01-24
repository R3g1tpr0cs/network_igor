from .models import Commands
from django.forms import ModelForm, TextInput

class CommandsForm(ModelForm):
    class Meta:
        fields = ['input', 'output']
        
        widgets = {
            "input": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ввод команд'
            }),
            "output": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вывод результата'
            }),
        }