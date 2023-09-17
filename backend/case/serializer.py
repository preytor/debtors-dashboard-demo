from rest_framework import serializers

from .models import Case

class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = ('id', 'debtor', 'assigned_worker', 'case_status')