from rest_framework import serializers

from worker.serializer import CaseWorkerSerializer
from debtors.serializer import CaseDebtorSerializer
from .models import Case

class CaseSerializer(serializers.ModelSerializer):
    #debtor_name = serializers.ReadOnlyField(source='debtor.name')
    #worker_name = serializers.ReadOnlyField(source='assigned_worker.name')
    assigned_worker = CaseWorkerSerializer(read_only=True)
    debtor = CaseDebtorSerializer(read_only=True)
    class Meta:
        model = Case
        fields = ('id', 
                  'debtor',
                  'assigned_worker',
                  'case_status', 
                  'borrowed_amount', 
                  'payment_frequency', 
                  'interest_rate', 
                  'amortization_period', 
                  'created_at')
        