from django import forms
from apps.pbv.models import pbv

class prueba(forms.ModelForm):
    class Meta:
        model = pbv
        fields = [
            'marca',
            'modelo',
            'cc',
            'especificaciones',
        ]
        labels = {
            'marca': 'Marca' ,
            'modelo': 'Modelo',
            'cc': 'Cilindraje',
            'especificaciones': 'Especificaciones',
        }
        widgets = {
            'marca': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Toyota'}),
            'modelo' :forms.TextInput(attrs={'class': 'form-control','placeholder':'Rav-4.1'}),
            'cc' :forms.NumberInput(attrs={'class': 'form-control'}),
            'especificaciones': forms.TextInput(attrs={'class': 'form-control'}),
            
        }