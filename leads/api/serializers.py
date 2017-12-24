from rest_framework import serializers
import re

from leads.models import Join


class JoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Join
        fields = ['lead_name', 'telephone']

    def validate_lead_name(self, value):
        lead_name = value
        pattern_name = '[а-яА-Я ]'
        if re.search(pattern_name, lead_name):
            return lead_name
        else:
            raise serializers.ValidationError("Введите правильное имя")


    def validate_telephone(self, value):
        telephone = value
        pattern_telephone = '((8|\+?375)[\- ]?)?(\(?\d{2,3}\)?[\- ]?)?[\d\- ]{7,10}'
        if re.search(pattern_telephone, telephone):
            return telephone
        else:
            raise serializers.ValidationError("Введите правильный телефон")

    # def validate(self, value):
    #     lead_name = value['lead_name']
    #     telephone = value['telephone']