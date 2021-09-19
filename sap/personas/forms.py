from django.forms import ModelForm, EmailInput
from personas.models import Persona

#Personalizar formularios
class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type':'email'})
        }
