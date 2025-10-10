from django import forms
from .models import Country

class CountryForm(forms.ModelForm):
    class Meta:
      model = Country
      fields = ['name', 'abrev']
      widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'abrev': forms.TextInput(attrs={'class': 'form-control'}),
}