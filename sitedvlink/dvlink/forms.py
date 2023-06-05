from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import *
from django.contrib.auth.models import User


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


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Логин'
    }))
    email = forms.CharField(max_length=255, widget=forms.EmailInput(attrs={
        'placeholder': 'E-mail'
    }))
    password1 = forms.CharField(max_length=18, widget=forms.PasswordInput(attrs={
        'pattern': '(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,}',
        'placeholder': 'Пароль'
    }))
    password2 = forms.CharField(max_length=18, widget=forms.PasswordInput(attrs={
        'pattern': '(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,}',
        'placeholder': 'Повторите пароль'
    }))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Логин'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Пароль'
    }))

    class Meta:
        model = User
        fields = ('username', 'password')

