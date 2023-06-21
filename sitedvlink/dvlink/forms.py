from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.validators import RegexValidator

from .models import *
from django.contrib.auth.models import User


class AddAppliForm(forms.Form):
    field_fio = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'placeholder': 'ФИО'
    }))
    field_number_phone = forms.CharField(max_length=18, widget=forms.TextInput(attrs={
        'placeholder': 'Телефон', 'onkeypress': 'return/[0-9+( )-]/i.test(event.key)',
        'pattern': r'\+7 \(\d{3}\) \d{3}-\d{2}-\d{2}',
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


class AddAppliAccForm(forms.ModelForm):
    field_text_appeal = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Текст обращения'
    }))
    field_organisation_name = forms.CharField(widget=forms.HiddenInput())
    field_email = forms.CharField(widget=forms.HiddenInput())
    field_number_phone = forms.CharField(widget=forms.HiddenInput())
    field_fio = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        model = Applications
        fields = ('field_text_appeal', )

    def __init__(self, *args, **kwargs):
        profile = kwargs.pop('profile', None)
        super().__init__(*args, **kwargs)
        if profile:
            self.fields['field_organisation_name'].initial = profile.organisation_name
            self.fields['field_email'].initial = profile.user.email
            self.fields['field_number_phone'].initial = profile.number_phone
            self.fields['field_fio'].initial = profile.user.username


class RegisterUserForm(UserCreationForm):
    password_validator = RegexValidator(
        regex=r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,}$'
    )
    username = forms.CharField(strip=True, widget=forms.TextInput(attrs={
        'placeholder': 'Логин'
    }))
    email = forms.CharField(max_length=255, widget=forms.EmailInput(attrs={
        'placeholder': 'E-mail'
    }))
    password1 = forms.CharField(validators=[password_validator], max_length=255, widget=forms.PasswordInput(attrs={
        'placeholder': 'Пароль'
    }))
    password2 = forms.CharField(validators=[password_validator], max_length=255, widget=forms.PasswordInput(attrs={
        'placeholder': 'Повторите пароль'
    }))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Пароли не совпадают')

        return cleaned_data



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


class ProfileForm(forms.ModelForm):
    organisation_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Название организации'
    }))
    number_phone = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Телефон', 'onkeypress': 'return/[0-9+( )-]/i.test(event.key)',
        'pattern': r'\+7 \(\d{3}\) \d{3}-\d{2}-\d{2}',
    }))

    class Meta:
        model = Profile
        fields = ('organisation_name', 'number_phone')
