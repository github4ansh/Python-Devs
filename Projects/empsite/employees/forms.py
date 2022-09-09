from django import forms
from django.forms import ModelForm
from .models import Employee


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee

        fields = ('first_name', 'last_name', 'designation', 'level', 'email_id')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'designation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Designation'}),
            'level': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Level'}),
            'email_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email ID'}),
        }
