from django import forms
from .models import Payment

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('case', 'payment_date', 'payment_amount', 'payment_status')
        labels = {
            'case': 'Case',
            'payment_date': 'Payment Date',
            'payment_amount': 'Payment Amount',
            'payment_status': 'Payment Status',
        }

        PAYMENT_CHOICES = Payment.payment_status.field.choices
        payment_status = forms.ChoiceField(choices=PAYMENT_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

        widgets = {
            'case': forms.Select(attrs={'class': 'form-control'}),
            'payment_date': forms.DateInput(attrs={'class': 'form-control'}),
            'payment_amount': forms.NumberInput(attrs={'class': 'form-control'}),
        }
