# forms.py

from django import forms
from .models import Coordinator

class CoordinatorCreationForm(forms.ModelForm):
    class Meta:
        model = Coordinator
        fields = ['F_NAME', 'F_PHONE_NO', 'F_EMAIL', 'F_DEPARTMENT', 'F_Personal_Email', 'F_ID', 'F_INSTITUTE']
