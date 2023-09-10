from django.urls import path
from .views import *

urlpatterns = [
    path('worker', WorkerView.as_view({
        'post': 'create_worker',
        'get': 'list_workers'
    }), name='list_workers'),
    path('worker/<str:pk>', WorkerView.as_view({
        'get': 'get_worker_data',
        'put': 'update_worker_data',
        'delete': 'delete_worker_data'
    }), name='worker_data'),
]