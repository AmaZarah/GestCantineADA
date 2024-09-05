from django import forms
from .models import PlatModel


#create your forms


class PlatForm(forms.ModelForm):
    class Meta:
        model = PlatModel
        fields = '__all__'