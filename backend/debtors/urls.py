from django.urls import path
from .views import *

urlpatterns = [
    path('debtors', DebtorViewSet.as_view({
        'get': 'list_debtors',
    }), name='debtors'),
    path('debtor', DebtorView.as_view({
        'post': 'create_debtor',
    }), name='debtor_data'),
    path('debtor/<str:pk>', DebtorView.as_view({
        'get': 'get_debtor_data',
        'put': 'update_debtor_data',
        'delete': 'delete_debtor_data'
    }), name='debtor_data'),
]