from django import forms
from .models import *

class AddAppliForm(forms.Form):
    field_fio = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'placeholder': 'ФИО'
    }))
    field_number_phone = forms.CharField(max_length=18, widget=forms.TextInput(attrs={
        'placeholder': 'Телефон', 'onkeypress': 'return/[0-9+( )-]/i.test(event.key)', 'pattern': '(?=.*[0-9]).{18}'
    }))
    field_email = forms.EmailField(max_length=255, widget=forms.EmailInput(attrs={
        'placeholder': "E-mail"
    }))
    field_organisation_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'placeholder': 'Название организации'
    }))
    field_text_appeal = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Текст обращения'
    }))

    class Meta:
        model = Applications
        fields = ('field_fio', 'field_number_phone', 'field_email', 'field_organisation_name', 'field_text_appeal')
