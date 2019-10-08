from django import forms
from .models import Zakaz

class ZakazCreateForm(forms.ModelForm):
    class Meta:
        model = Zakaz
        fields = [
            'first_name',
            'email',
            'body_zakaz'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': '', 'class': 'form-control rows=3'}),
            'body_zakaz': forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': '', 'class': 'form-control rows=3'}),
        }