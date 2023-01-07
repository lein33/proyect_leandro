from django import forms
from apps.vehiculo.models import Vehiculo, Mantenimiento

class MantenimientoForm(forms.ModelForm):
    class Meta:
        model = Mantenimiento
        fields = [
            'descipcion',
            'fecha', 
        ]
        labels = {
            'descipcion': 'Placa',
            'fecha': 'Marca',
        }
        widgets = {
            'descipcion': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha' :forms.DateField(),     
        }

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = [
            'placa',
            'marca',
            'modelo',
            'tipo',
            'color',
            'cc',
            'mantenimiento',
            
        ]
        labels = {
            'placa': 'Placa',
            'marca': 'Marca',
            'modelo': 'Modelo',
            'tipo': 'Tipo',
            'color': 'Color',
            'cc': 'Cilindraje',
            'mantenimiento': 'Mantenimiento',
        }
        widgets = {
            'placa': forms.TextInput(attrs={'class': 'form-control'}),
            'marca' :forms.TextInput(attrs={'class': 'form-control'}),
            'modelo' :forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'cc' :forms.TextInput(attrs={'class': 'form-control'}) ,
            'mantenimiento': forms.CheckboxSelectMultiple(),
            
        }

