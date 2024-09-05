from django import forms
from .models import MenuMolel


#create your forms


class MenuForm(forms.ModelForm):
    class Meta:
        model = MenuMolel
        fields = '__all__'