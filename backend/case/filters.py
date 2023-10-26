from rest_framework import filters
from django.contrib import admin
from advanced_filters.admin import AdminAdvancedFiltersMixin

class CaseFilter(filters.BaseFilterBackend):
    
    def filter_queryset(self, request, queryset, view):
        debtor = request.query_params.get('debtor', None)
        assigned_worker = request.query_params.get('assigned_worker', None)
        case_status = request.query_params.get('case_status', None)

        borrowed_amount = request.query_params.get('borrowed_amount', None)
        borrowed_amount_gt = request.query_params.get('borrowed_amount_gt', None)
        borrowed_amount_gte = request.query_params.get('borrowed_amount_gte', None)
        borrowed_amount_lt = request.query_params.get('borrowed_amount_lt', None)
        borrowed_amount_lte = request.query_params.get('borrowed_amount_lte', None)

        payment_frequency = request.query_params.get('payment_frequency', None)

        interest_rate = request.query_params.get('interest_rate', None)
        interest_rate_gt = request.query_params.get('interest_rate_gt', None)
        interest_rate_gte = request.query_params.get('interest_rate_gte', None)
        interest_rate_lt = request.query_params.get('interest_rate_lt', None)
        interest_rate_lte = request.query_params.get('interest_rate_lte', None)

        amortization_period = request.query_params.get('amortization_period', None)
        amortization_period_gt = request.query_params.get('amortization_period_gt', None)
        amortization_period_gte = request.query_params.get('amortization_period_gte', None)
        amortization_period_lt = request.query_params.get('amortization_period_lt', None)
        amortization_period_lte = request.query_params.get('amortization_period_lte', None)

        created_at = request.query_params.get('created_at', None)
        created_at_gt = request.query_params.get('created_at_gt', None)
        created_at_gte = request.query_params.get('created_at_gte', None)
        created_at_lt = request.query_params.get('created_at_lt', None)
        created_at_lte = request.query_params.get('created_at_lte', None)

        ordering = request.query_params.get('ordering', None)

        if debtor:
            queryset = queryset.filter(debtor=debtor)

        if assigned_worker:
            queryset = queryset.filter(assigned_worker=assigned_worker)

        if case_status:
            queryset = queryset.filter(case_status=case_status)

        if borrowed_amount:
            queryset = queryset.filter(borrowed_amount=borrowed_amount)
        if borrowed_amount_gt:
            queryset = queryset.filter(borrowed_amount__gt=borrowed_amount_gt)
        if borrowed_amount_gte:
            queryset = queryset.filter(borrowed_amount__gte=borrowed_amount_gte)
        if borrowed_amount_lt:
            queryset = queryset.filter(borrowed_amount__lt=borrowed_amount_lt)
        if borrowed_amount_lte:
            queryset = queryset.filter(borrowed_amount__lte=borrowed_amount_lte)

        if payment_frequency:
            queryset = queryset.filter(payment_frequency=payment_frequency)

        if interest_rate:
            queryset = queryset.filter(interest_rate=interest_rate)
        if interest_rate_gt:
            queryset = queryset.filter(interest_rate__gt=interest_rate_gt)
        if interest_rate_gte:
            queryset = queryset.filter(interest_rate__gte=interest_rate_gte)
        if interest_rate_lt:
            queryset = queryset.filter(interest_rate__lt=interest_rate_lt)
        if interest_rate_lte:
            queryset = queryset.filter(interest_rate__lte=interest_rate_lte)

        if amortization_period:
            queryset = queryset.filter(amortization_period=amortization_period)
        if amortization_period_gt:
            queryset = queryset.filter(amortization_period__gt=amortization_period_gt)
        if amortization_period_gte:
            queryset = queryset.filter(amortization_period__gte=amortization_period_gte)
        if amortization_period_lt:
            queryset = queryset.filter(amortization_period__lt=amortization_period_lt)
        if amortization_period_lte:
            queryset = queryset.filter(amortization_period__lte=amortization_period_lte)

        if created_at:
            queryset = queryset.filter(created_at=created_at)
        if created_at_gt:
            queryset = queryset.filter(created_at__gt=created_at_gt)
        if created_at_gte:
            queryset = queryset.filter(created_at__gte=created_at_gte)
        if created_at_lt:
            queryset = queryset.filter(created_at__lt=created_at_lt)
        if created_at_lte:
            queryset = queryset.filter(created_at__lte=created_at_lte)

        if ordering:
            queryset = queryset.order_by(ordering)
        else:
            queryset = queryset.order_by('id')
        return queryset

    
class DebtorIdAdminFilter(admin.SimpleListFilter):
    title = 'Debtor'
    parameter_name = 'debtor'

    def lookups(self, request, model_admin):
        return (
            (None, None),
        )
    
    def choices(self, changelist):
        query_params = changelist.get_filter_params()
        query_params.pop(self.parameter_name, None)
        all_choice = next(super().choices(changelist))
        all_choice['query_params'] = query_params
        yield all_choice

    def queryset(self, request, queryset):
        debtor_id = self.value()
        if debtor_id:
            return queryset.filter(debtor__id=debtor_id)
        
            
class AssignedWorkerAdminFilter(admin.SimpleListFilter):
    title = 'Assigned Worker'
    parameter_name = 'assigned_worker'

    def lookups(self, request, model_admin):
        return (
            (None, None),
        )

    def queryset(self, request, queryset):
        assigned_worker_id = self.value()
        if assigned_worker_id:
            # Ensure the input value is a valid integer before filtering
            try:
                assigned_worker_id = int(assigned_worker_id)
            except ValueError:
                return queryset.none()  # Return an empty queryset for non-integer input

            return queryset.filter(assigned_worker__id=assigned_worker_id)
        return queryset
        

class CaseStatusAdminFilter(admin.SimpleListFilter):
    title = 'case status'
    parameter_name = 'case_status'

    def lookups(self, request, model_admin):
        return (
            ('open', 'Open'),
            ('closed', 'Closed'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'open':
            return queryset.filter(case_status='open')
        if self.value() == 'closed':
            return queryset.filter(case_status='closed')