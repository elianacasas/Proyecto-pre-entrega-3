from django import forms
 
class AgregarFormulario(forms.Form):
    name = forms.CharField()
    direccion = forms.CharField()
    horario = forms.CharField()
    descripcion = forms.CharField()
    
    
class SuscribirseFormulario(forms.Form):
    username = forms.CharField()
    email = forms.CharField()
    password = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    
class BuscarCafeterias(forms.Form):
    direccion = forms.CharField()

class ReseñaFormulario(forms.Form):
    name = forms.CharField()
    opinion = forms.CharField()
    puntaje = forms.IntegerField()
    
    