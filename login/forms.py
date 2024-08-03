from django import forms
from .models import *

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Chat_signup
        fields = ['first_name', 'last_name', 'email', 'username', 'password','role']
