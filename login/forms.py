from django import forms
from .models import *

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = signup_data
        fields = ['first_name', 'last_name', 'email', 'username', 'password','role']


class OrganizationForm(forms.ModelForm):
    class Meta :
        model = Organizations_data
        fields = ['Gst_no','Company_name','Domain','Address','city','State','Pincode','contact_info']
        