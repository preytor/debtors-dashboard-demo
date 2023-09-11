from django import forms
from .models import Worker

class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ('name', 'contact_info', 'role')
        labels = {
            'name': 'Name',
            'contact_info': 'Contact Info',
            'role': 'Role',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_info': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.TextInput(attrs={'class': 'form-control'}),
        }