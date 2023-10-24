# forms.py

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Coordinator,Student


class CoordinatorCreationForm(forms.ModelForm):
    class Meta:
        model = Coordinator
        fields = ['F_NAME', 'F_PHONE_NO', 'F_EMAIL', 'F_DEPARTMENT', 'F_Personal_Email', 'F_ID', 'F_INSTITUTE']




class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'  # Use all fields from the model
        Diploma_percentage = forms.DecimalField(required=False)
        
    

class StudentLoginForm(AuthenticationForm):
    # Additional fields for Student login (PRN)
    s_prn = forms.CharField(label="PRN", max_length=12)







