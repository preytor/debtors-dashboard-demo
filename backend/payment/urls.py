from django.urls import path
from .views import *

urlpatterns = [
    path('payments/<str:debtor_id>', PaymentViewSet.as_view({
        'get': 'list_payments',
    }), name='payments'),
    path('payment', PaymentView.as_view({
        'post': 'create_payment',
    }), name='payment_data'),
    path('payment/<str:pk>', PaymentView.as_view({
        'get': 'get_payment_data',
        'put': 'update_payment_data',
        'delete': 'delete_payment_data'
    }), name='payment_data'),
]