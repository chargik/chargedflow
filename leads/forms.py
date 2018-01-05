from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from .models import Join


def validate_lead_name(value):
    lead_name_validator = RegexValidator(regex='^[а-яА-ЯёЁ ]+$')
    try:
        lead_name_validator(value)
    except:
        raise ValidationError("Введите правильное имя")
    return value

def validate_telephone(value):
    telephone_validator = RegexValidator(regex='((8|\+?375)[\- ]?)?(\(?\d{2,3}\)?[\- ]?)?[\d\- ]{7,10}')
    try:
        telephone_validator(value)
    except:
        raise ValidationError("Введите правильный телефон")
    return value


class JoinForm(forms.ModelForm):
    lead_name = forms.CharField(label='', required=True, validators=[validate_lead_name],
            widget=forms.TextInput(
                attrs={'placeholder': 'Ваше Имя', 'class': 'form-control', 'id': 'lead_name'}
                ))
    telephone = forms.CharField(label='', required=True, validators=[validate_telephone],
            widget=forms.TextInput(
                attrs={'placeholder': 'Ваш личный телефон', 'class': 'form-control', 'type': 'tel', 'id': 'telephone'}
                ))
    class Meta:
        model = Join
        fields = ['lead_name', 'telephone']