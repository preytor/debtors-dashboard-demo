from django import forms
from .models import Case

class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ('debtor', 'assigned_worker', 'case_status')
        labels = {
            'debtor': 'Debtor',
            'assigned_worker': 'Assigned Worker',
            'case_status': 'Case Status',
        }

        CASE_CHOICES = Case.case_status.field.choices
        case_status = forms.ChoiceField(choices=CASE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

        widgets = {
            'debtor': forms.Select(attrs={'class': 'form-control'}),
            'assigned_worker': forms.Select(attrs={'class': 'form-control'}),
        }