from django import forms
from django.conf import settings
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

    def form_valid(self, form):
        lead_name = form.cleaned_data.get("lead_name")
        telephone = form.cleaned_data.get("telephone")
        # instance = form.save(commit=False)
        # instance.save()
        # new_contact = BaseContact(lead_name=lead_name, phone=telephone)
        # new_contact.save()
        subject = 'Заявка с сайта'
        message = '''Заявка со страницы {0} \n\n
        Имя: {1}\n\n
        Телефон:{2}\n\n'''.format(self.request.path_info, form.cleaned_data['lead_name'], form.cleaned_data['telephone'])
        from_email = settings.EMAIL_HOST_USER
        to_email = ['unklerufus@gmail.com']
        send_mail(subject, message, from_email, to_email, fail_silently=True)
        # add amocrm
        return HttpResponseRedirect(self.request.path_info)