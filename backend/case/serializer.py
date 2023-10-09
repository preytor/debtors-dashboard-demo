from rest_framework import serializers

from .models import Case, CaseView

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
        
class CaseViewSerializer(serializers.ModelSerializer):

    #assigned_worker_name = serializers.CharField(source='assigned_worker.name', read_only=True)
    #debtor_name = serializers.CharField(source='debtor.name', read_only=True)

    class Meta:
        model = CaseView
        fields = ('id',
                  'assigned_worker',
                  'assigned_worker_name',
                  'debtor',
                  'debtor_name',
                  'case_status',
                  'borrowed_amount',
                  'payment_frequency',
                  'interest_rate',
                  'amortization_period',
                  'created_at')
