from django import forms
from .models import *

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = signup_data
        fields = ['first_name', 'last_name', 'email', 'username', 'password','role']


class AllocationForm(forms.ModelForm):
    class Meta :
        model =  Allocation
        fields = ['user','Startup_name','contact_info']