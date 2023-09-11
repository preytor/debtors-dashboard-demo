from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response

from .models import Worker
from .forms import WorkerForm
from .serializer import WorkerSerializer
from .filters import WorkerFilter

# Create your views here.
# We get a filtered view for the worker
class WorkerViewSet(viewsets.ModelViewSet):
    
    def list_workers(self, request):
        print("request", request.query_params)
        self.filterset_class = WorkerFilter
        queryset = Worker.objects.all()
        name = self.request.query_params.get('name', None)
        role = self.request.query_params.get('role', None)

        if name is not None:
            queryset = queryset.filter(name=name)
        if role is not None:
            queryset = queryset.filter(role=role)
        print("queryset", queryset)
        serializer = WorkerSerializer(queryset, many=True)
        return Response(serializer.data)

# We do a crud of the worker with a view
class WorkerView(viewsets.ModelViewSet):
    # Create
    def create_worker(self, request):
        form = WorkerForm(request.POST)
        if form.is_valid():
            form.save()
        return Response("Item successfully created")
    
    # Read
    def list_workers(self, request):
        print("list_workers", request.data)
        workers = Worker.objects.all()
        print("workers", workers)
        serializer = WorkerSerializer(workers, many=True)
        print("serializer", serializer)
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
        return Response("Item successfully deleted")
    