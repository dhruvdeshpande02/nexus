# forms.py

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Coordinator,Student,Notice


class CoordinatorCreationForm(forms.ModelForm):
    class Meta:
        model = Coordinator
        fields = '__all__' 




class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'  # Use all fields from the model
        Diploma_percentage = forms.DecimalField(required=False)
        exclude = ['AVG TILL SEM cgpa', 'AVG TILL SEM percentage'] 
        
    

class StudentLoginForm(forms.Form):
    S_PRN = forms.IntegerField()
    s_password = forms.CharField(widget=forms.PasswordInput)
    




class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice  # Specify the model the form is based on
        fields = ['notice_id','notice_type', 'title', 'content', 'file','applicants']  # Define the fields to include in the form
        
        

    # You can add custom form field attributes or validation here if needed

class CoordinatorLoginForm(forms.Form):
    F_ID = forms.CharField(max_length=100)
    f_password = forms.CharField(widget=forms.PasswordInput)


class TnpAdminLoginForm(AuthenticationForm):
    # Add any additional fields or customization here
    # For example, you can add a label to the username field:
    username = forms.CharField(label='Username')

from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['application_status']




