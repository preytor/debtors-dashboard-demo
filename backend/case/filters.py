from django_filters import rest_framework as filters

from backend_debtors.filters import LikeFilter
from .models import Case

class CaseFilter(filters.FilterSet):

    debtor = filters.NumberFilter(field_name='debtor__id')
    assigned_worker = filters.NumberFilter(field_name='assigned_worker__id')
    case_status = LikeFilter(field_name='case_status')
    case_status__in = filters.BaseInFilter(field_name='case_status', lookup_expr='in')

    class Meta:
        model = Case
        fields = ['debtor', 'assigned_worker', 'case_status']