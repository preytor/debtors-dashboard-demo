from rest_framework import filters

class DebtorFilter(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        name = request.query_params.get('name', None)
        contact_info = request.query_params.get('contact_info', None)
        legal_status = request.query_params.get('legal_status', None)
        ordering = request.query_params.get('ordering', None)
        if name:
            queryset = queryset.filter(name__icontains=name)
        if contact_info:
            queryset = queryset.filter(contact_info__icontains=contact_info)
        if legal_status:
            queryset = queryset.filter(legal_status=legal_status)
        if ordering:
            queryset = queryset.order_by(ordering)
        else:
            queryset = queryset.order_by('id')
        return queryset
