from rest_framework import filters

class CaseFilter(filters.BaseFilterBackend):
    
    def filter_queryset(self, request, queryset, view):
        debtor = request.query_params.get('debtor', None)
        assigned_worker = request.query_params.get('assigned_worker', None)
        case_status = request.query_params.get('case_status', None)
        borrowed_amount = request.query_params.get('borrowed_amount', None)
        payment_frequency = request.query_params.get('payment_frequency', None)
        interest_rate = request.query_params.get('interest_rate', None)
        amortization_period = request.query_params.get('amortization_period', None)
        created_at = request.query_params.get('created_at', None)

        if debtor:
            queryset = queryset.filter(debtor__id=debtor)
        if assigned_worker:
            queryset = queryset.filter(assigned_worker__id=assigned_worker)
        if case_status:
            queryset = queryset.filter(case_status=case_status)
        if borrowed_amount: # exact, gt, gte, lt, lte
            queryset = queryset.filter(borrowed_amount=borrowed_amount)
        if payment_frequency:
            queryset = queryset.filter(payment_frequency=payment_frequency)
        if interest_rate: # exact, gt, gte, lt, lte
            queryset = queryset.filter(interest_rate=interest_rate)
        if amortization_period: # exact, gt, gte, lt, lte
            queryset = queryset.filter(amortization_period=amortization_period)
        if created_at: # exact, gt, gte, lt, lte
            queryset = queryset.filter(created_at=created_at)
        return queryset
    