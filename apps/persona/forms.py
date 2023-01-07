from django import forms
from apps.persona.models import Persona

class PersonaFrom(forms.ModelForm):
    #required_css_class = "hola"
    class Meta:
        model = Persona
        fields = [
            'dni',
            'nombre',
            'edad',
            'sexo',
            'correo',
            'pais',
            'provincia',
            'direccion',
            'cod_postal',
            'celular',
        ]
        labels = {
            'dni': 'Cedula' ,
            'nombre': 'Nombre',
            'edad': 'Edad',
            'sexo': 'Sexo',
            'correo': 'Email',
            'pais': 'País',
            'provincia': 'Provincia',
            'direccion': 'Direccion',
            'cod_postal': 'Codigo Postal',
            'celular': 'Celular', 
        }
        widgets = {
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre' :forms.TextInput(attrs={'class': 'form-control'}),
            'edad' :forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'pais' :forms.TextInput(attrs={'class': 'form-control'}) ,
            'provincia':forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'cod_postal': forms.TextInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),
        }