from rest_framework import serializers

from .models import Debtor

class DebtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debtor
        fields = ('id', 'name', 'contact_info', 'legal_status')