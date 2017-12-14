from rest_framework import serializers


from leads.models import Join


class JoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Join
        fields = ['name', 'telephone']

    def validate_name(self, value):
        name = value
        pattern = '[а-яА-Я ]{1,20}'
        if re.search(pattern, name):
            return name
        else:
            raise serializers.ValidationError("Введите правильное имя")


    def validate_telephone(self, value):
        telephone = value
        pattern = '((8|\+?375)[\- ]?)?(\(?\d{2,3}\)?[\- ]?)?[\d\- ]{7,10}'
        if re.search(pattern, telephone):
            return telephone
        else:
            raise serializers.ValidationError("Введите парвильный телефон")