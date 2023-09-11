from django_filters import rest_framework as filters

from backend_debtors.filters import LikeFilter

class WorkerFilter(filters.FilterSet):

    name = LikeFilter(field_name='name')
    contact_info = LikeFilter(field_name='contact_info')
    role = LikeFilter(field_name='role')
