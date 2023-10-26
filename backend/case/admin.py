from django.contrib import admin
from advanced_filters.admin import AdminAdvancedFiltersMixin
from .models import Case
from .filters import DebtorIdAdminFilter, AssignedWorkerAdminFilter, CaseStatusAdminFilter
from .forms import CaseForm

# Register your models here.
class CaseAdmin(AdminAdvancedFiltersMixin, admin.ModelAdmin):
    list_display = (
        'id',
        'debtor_name',
        'assigned_worker_name',
        'case_status',
        'borrowed_amount',
        'payment_frequency',
        'interest_rate',
        'amortization_period',
        'created_at',
    )

    list_filter = (
        'case_status',
        'payment_frequency',
    )
    
    advanced_filter_fields = (
        'debtor__id',
        'debtor__name',
        'assigned_worker__id',
        'assigned_worker__name',
        'case_status',
        'borrowed_amount',
        'payment_frequency',
        'interest_rate',
        'amortization_period',
        'created_at',
    )

    """
    list_filter = (
        'debtor',
        'assigned_worker',
        'case_status',
        'borrowed_amount',
        'payment_frequency',
        'interest_rate',
        'amortization_period',
        'created_at',
    )
    """

    def debtor_name(self, obj):
        return f'{obj.debtor.name} (id: {obj.debtor.id})'
    
    def assigned_worker_name(self, obj):
        return f'{obj.assigned_worker.name} (id: {obj.assigned_worker.id})'

    form = CaseForm

# Register the Case model with the custom admin class
admin.site.register(Case, CaseAdmin)
