from django.urls import path
from .views import *

urlpatterns = [
    path('cases', CaseViewSet.as_view({
        'get': 'list_cases',
    }), name='cases'),
    path('case', CaseView.as_view({
        'post': 'create_case',
    }), name='case_data'),
    path('case/<str:pk>', CaseView.as_view({
        'get': 'get_case_data',
        'put': 'update_case_data',
        'delete': 'delete_case_data'
    }), name='case_data'),
]