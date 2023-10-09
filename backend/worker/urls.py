from django.urls import path
from .views import *

urlpatterns = [
    path('workers', WorkerViewSet.as_view()),
    path('worker', WorkerView.as_view({
        'post': 'create_worker',
    }), name='worker_data'),
    path('worker/<str:pk>', WorkerView.as_view({
        'get': 'get_worker_data',
        'put': 'update_worker_data',
        'delete': 'delete_worker_data'
    }), name='worker_data'),
]