from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response

from .models import Worker
from .forms import WorkerForm
from .serializer import WorkerSerializer
from .filters import WorkerFilter

from backend_debtors.paginations import CustomPagination

# Create your views here.
# We get a filtered view for the worker
class WorkerViewSet(viewsets.ModelViewSet):

    pagination_class = CustomPagination
    
    def list_workers(self, request):
        self.filterset_class = WorkerFilter
        queryset = Worker.objects.order_by('id')
        name = self.request.query_params.get('name', None)
        role = self.request.query_params.get('role', None)

        if name is not None:
            queryset = queryset.filter(name=name)
        if role is not None:
            queryset = queryset.filter(role=role)

        # Define the number of items per page
        page = self.paginate_queryset(queryset)
        
        if page is not None:
            serializer = WorkerSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = WorkerSerializer(queryset, many=True)
        return Response(serializer.data)

# We do a crud of the worker with a view
class WorkerView(viewsets.ModelViewSet):
    # Create
    def create_worker(self, request):
        form = WorkerForm(request.POST)
        if form.is_valid():
            form.save()
        return Response(form.data, status=201)
    
    # Read
    def list_workers(self, request):
        workers = Worker.objects.all()
        serializer = WorkerSerializer(workers, many=True)
        return Response(serializer.data)
    
    def get_worker_data(self, request, pk):
        worker = get_object_or_404(Worker, id=pk)
        serializer = WorkerSerializer(worker, many=False)
        return Response(serializer.data)
    
    # Update
    def update_worker_data(self, request, pk):
        worker = get_object_or_404(Worker, id=pk)
        serializer = WorkerSerializer(instance=worker, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
    # Delete
    def delete_worker_data(self, request, pk):
        worker = get_object_or_404(Worker, id=pk)
        worker.delete()
        return Response(status=200)
    