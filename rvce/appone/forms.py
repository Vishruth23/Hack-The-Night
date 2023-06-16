from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = '__all__'

class NGO_RegForm(forms.ModelForm):
    class Meta:
        model = NGO
        fields = '__all__'
