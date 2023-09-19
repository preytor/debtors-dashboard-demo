from django_filters import rest_framework as filters

from backend_debtors.filters import LikeFilter
from .models import Debtor

class DebtorFilter(filters.FilterSet):

    name = LikeFilter(field_name='name')
    contact_info = LikeFilter(field_name='contact_info')
    legal_status = LikeFilter(field_name='legal_status')

    class Meta:
        model = Debtor
        fields = ['name', 'contact_info', 'legal_status']