from django import forms

from .models import Join

class JoinForm(forms.ModelForm):
    name = forms.CharField(label='',
            widget=forms.TextInput(
                attrs={'placeholder': 'Ваше Имя', 'class': 'form-control'}
                ))
    telephone = forms.CharField(label='',
            widget=forms.TextInput(
                attrs={'placeholder': 'Ваш личный телефон', 'class': 'form-control', 'type': 'tel'}
                ))
    class Meta:
        model = Join
        fields = ['name', 'telephone']