from django import forms
from .models import Feature


class FeatureForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = ( "feature_title", "details")