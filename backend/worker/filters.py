from rest_framework import filters

class WorkerFilter(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        name = request.query_params.get('name', None)
        contact_info = request.query_params.get('contact_info', None)
        roles = request.query_params.getlist('role', None)
        ordering = request.query_params.get('ordering', None)
        if name:
            queryset = queryset.filter(name__icontains=name)
        if contact_info:
            queryset = queryset.filter(contact_info__icontains=contact_info)
        if roles:
            queryset = queryset.filter(role__in=roles)
        if ordering:
            queryset = queryset.order_by(ordering)
        else:
            queryset = queryset.order_by('id')
        return queryset
