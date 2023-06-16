from .models import *
from django import forms

class studentinformationsforms(forms.ModelForm):
    class Meta:
        model = StudentDetail
        fields = "__all__"