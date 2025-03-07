from django import forms
from .models import Car, CarPhoto

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['category', 'make', 'model', 'year', 'description', 'price_per_day', 'license_plate']

class CarPhotoForm(forms.ModelForm):
    class Meta:
        model = CarPhoto
        fields = ['photo']

class RentalForm(forms.Form):
    start_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))