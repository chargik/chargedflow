from django import forms
import re
from .models import Join

class JoinForm(forms.ModelForm):
    name = forms.CharField(label='', required=True, 
            widget=forms.TextInput(
                attrs={'placeholder': 'Ваше Имя', 'class': 'form-control', 'id': 'name'}
                ))
    telephone = forms.CharField(label='', required=True,
            widget=forms.TextInput(
                attrs={'placeholder': 'Ваш личный телефон', 'class': 'form-control', 'type': 'tel', 'id': 'telephone'}
                ))
    class Meta:
        model = Join
        fields = ['name', 'telephone']  

    # def cleaned_data(self, *args, **kwargs):
    #     name = self.cleaned_data.get("name")
    #     telephone = self.cleaned_data.get("telephone")
    #     return name, telephone
    
    def clean_name(self, *args, **kwargs):
        name = self.cleaned_data.get('name')
        pattern = '[а-яА-я ]{1,20}'
        if re.search(pattern, name):
            return name
        else:
            raise forms.ValidationError("Введите правильное имя")

    def clean_telephone(self, *args, **kwargs):
        telephone = self.cleaned_data.get('telephone')
        # ^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$
        pattern = '((8|\+?375)[\- ]?)?(\(?\d{2,3}\)?[\- ]?)?[\d\- ]{7,10}'
        if re.search(pattern, telephone):
            return telephone
        else:
            raise forms.ValidationError("Введите парвильный телефон")