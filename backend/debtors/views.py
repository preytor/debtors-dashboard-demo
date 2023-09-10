
from rest_framework import viewsets
from rest_framework.response import Response

from worker.models import Worker
from .serializer import WorkerSerializer

# Create your views here.
# We do a crud of the worker with a view
class WorkerView(viewsets.ModelViewSet):
    # Create
    def create_worker(self, request):
        serializer = WorkerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
    # Read
    def list_workers(self, request):
        workers = Worker.objects.all()
        serializer = WorkerSerializer(workers, many=True)
        return Response(serializer.data)
    
    def get_worker_data(self, request, pk):
        worker = Worker.objects.get(id=pk)
        serializer = WorkerSerializer(worker, many=False)
        return Response(serializer.data)
    
    # Update
    def update_worker_data(self, request, pk):
        worker = Worker.objects.get(id=pk)
        serializer = WorkerSerializer(instance=worker, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
    # Delete
    def delete_worker_data(self, request, pk):
        worker = Worker.objects.get(id=pk)
        worker.delete()
        return Response("Item successfully deleted")
    