from django.forms import ModelForm,TextInput
from .models import Weather

class CityForm(ModelForm):
    class Meta:
        model=Weather
        fields=['name']
        widgets={'name':TextInput(attrs={'class':'form-control','placeholder':'City Name'})}