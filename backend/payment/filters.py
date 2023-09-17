from django_filters import rest_framework as filters

from backend_debtors.filters import LikeFilter
from .models import Payment

class PaymentFilter(filters.FilterSet):

    debtor = filters.NumberFilter(field_name='debtor__id')
    payment_date = LikeFilter(field_name='payment_date')
    payment_date__gte = filters.DateFilter(field_name='payment_date', lookup_expr='gte')
    payment_date__lte = filters.DateFilter(field_name='payment_date', lookup_expr='lte')
    payment_amount = LikeFilter(field_name='payment_amount')
    payment_amount__gt = filters.NumberFilter(field_name='payment_amount', lookup_expr='gt')
    payment_amount__lt = filters.NumberFilter(field_name='payment_amount', lookup_expr='lt')
    payment_status = LikeFilter(field_name='payment_status')

    class Meta:
        model = Payment
        fields = ['debtor', 'payment_date', 'payment_amount', 'payment_status']