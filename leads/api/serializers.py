from django.conf import settings
from django.core.mail import send_mail

from rest_framework import serializers
import re

from leads.models import Join

def send_join_mail(data):
    subject = 'Заявка с сайта'
    message = '''Заявка со страницы \n\n
    Имя: \n\n
    Телефон:{0}\n\n'''.format(data)
    from_email = settings.EMAIL_HOST_USER
    to_email = ['unklerufus@gmail.com']
    send_mail(subject, message, from_email, to_email, fail_silently=False)


class JoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Join
        fields = ['lead_name', 'telephone']


    def validate(self, data):
        lead_name = data['lead_name']
        telephone = data['telephone']
        pattern_name = '^[а-яА-ЯёЁ ]+$'
        pattern_phone = '((8|\+?375)[\- ]?)?(\(?\d{2,3}\)?[\- ]?)?[\d\- ]{7,10}'
        if not re.search(pattern_name, lead_name):
            raise serializers.ValidationError("Введите правильное имя")
        elif not re.search(pattern_phone, telephone):
            raise serializers.ValidationError("Введите правильный телефон")
        else:
            send_join_mail(data)
            # subject = 'Заявка с сайта'
            # message = '''Заявка со страницы \n\n
            # Имя:\n\n
            # Телефон:{0}\n\n'''.format(data)
            # from_email = settings.EMAIL_HOST_USER
            # to_email = ['unklerufus@gmail.com']
            # send_mail(subject, message, from_email, to_email, fail_silently=False)
            return data

