from django import forms
from .models import Debtor

class DebtorForm(forms.ModelForm):
    class Meta:
        model = Debtor
        fields = ('name', 'contact_info', 'legal_status')
        labels = {
            'name': 'Name',
            'contact_info': 'Contact Info',
            'legal_status': 'Legal Status',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_info': forms.TextInput(attrs={'class': 'form-control'}),
            'legal_status': forms.TextInput(attrs={'class': 'form-control'}),
        }