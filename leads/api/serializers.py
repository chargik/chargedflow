from rest_framework import serializers
import re

from leads.models import Join


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
            return data