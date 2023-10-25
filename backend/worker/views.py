from django.shortcuts import get_object_or_404

from rest_framework import viewsets, generics
from rest_framework.response import Response
from .models import Worker
from .forms import WorkerForm
from .serializer import WorkerSerializer
from .filters import WorkerFilter

from backend_debtors.paginations import CustomPagination

# Create your views here.
# We get a filtered view for the worker
class WorkerViewSet(generics.ListAPIView):

    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    pagination_class = CustomPagination
    filter_backends = (WorkerFilter,)
    
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())

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
        return Response(form.errors, status=400)
    
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
    