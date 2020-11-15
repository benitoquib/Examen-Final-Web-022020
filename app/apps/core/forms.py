from django import forms
from .models import Product
class Productform(forms.ModelForm):
    class Meta:
        model=Product
        fields = [
            'name',
            'categoria',
            'pcompra',
            'pventa',
        ]
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                }
            ),
            'categoria': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese categoria',
                }
            ),
        }