from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
import re

from .models import Join

# BLACK_PHONE_LIST = ['5403311', '7502020']

def validate_lead_name(value):
    lead_name_validator = RegexValidator(regex='[а-яА-Я ]')
    try:
        lead_name_validator(value)
    except:
        raise ValidationError("Введите правильное имя")
    return value

def validate_telephone(value):
    clean_lead_phone = re.compile('[^0-9]')
    lead_name_validator = RegexValidator(regex='((8|\+?375)[\- ]?)?(\(?\d{2,3}\)?[\- ]?)?[\d\- ]{7,10}')
    if 
    try:
        lead_name_validator(value)
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

    # def cleaned_data(self, *args, **kwargs):
    #     name = self.cleaned_data.get("name")
    #     telephone = self.cleaned_data.get("telephone")
    #     return name, telephone
    
    # def clean_lead_name(self, *args, **kwargs):
    #     lead_name = self.cleaned_data.get('lead_name')
    #     pattern = '[а-яА-Я ]{1,20}'
    #     if re.search(pattern, lead_name):
    #         return lead_name
    #     else:
    #         raise forms.ValidationError("Введите правильное имя")

    # def clean_telephone(self, *args, **kwargs):
    #     telephone = self.cleaned_data.get('telephone')
    #     # ^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$
    #     pattern = '((8|\+?375)[\- ]?)?(\(?\d{2,3}\)?[\- ]?)?[\d\- ]{7,10}'
    #     if re.search(pattern, telephone):
    #         return telephone
    #     else:
    #         raise forms.ValidationError("Введите правильный телефон")