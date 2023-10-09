from rest_framework import serializers

from .models import Case

class CaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Case
        fields = ('id', 
                  'assigned_worker',
                  'debtor',
                  'case_status', 
                  'borrowed_amount', 
                  'payment_frequency', 
                  'interest_rate', 
                  'amortization_period', 
                  'created_at')