from django_filters import rest_framework as filters

from backend_debtors.filters import LikeFilter
from .models import Debtor

class DebtorFilter(filters.FilterSet):

    name = LikeFilter(field_name='name')
    contact_info = LikeFilter(field_name='contact_info')
    
    initial_debt = filters.NumberFilter()
    initial_debt__gt = filters.NumberFilter(field_name='initial_debt', lookup_expr='gt')
    initial_debt__lt = filters.NumberFilter(field_name='initial_debt', lookup_expr='lt')

    legal_status = LikeFilter(field_name='legal_status')

    class Meta:
        model = Debtor
        fields = ['name', 'contact_info', 'initial_debt', 'legal_status']