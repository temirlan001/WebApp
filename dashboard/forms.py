from django import forms
from .models import BrandData


class BrandDataFrom(forms.ModelForm):
    class Meta:
        model = BrandData
        fields = '__all__'
