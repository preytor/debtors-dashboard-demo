from django.shortcuts import get_object_or_404

from rest_framework import viewsets, generics
from rest_framework.response import Response

from .models import Debtor
from .forms import DebtorForm
from .serializer import DebtorSerializer
from .filters import DebtorFilter

from backend_debtors.paginations import CustomPagination

# Create your views here.
# We get a filtered view for the debtor
class DebtorViewSet(generics.ListAPIView):

    queryset = Debtor.objects.all()
    serializer_class = DebtorSerializer
    pagination_class = CustomPagination
    filter_backends = (DebtorFilter,)

    def list_debtors(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        # Define the number of items per page
        page = self.paginate_queryset(queryset)
        
        if page is not None:
            serializer = DebtorSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = DebtorSerializer(queryset, many=True)
        return Response(serializer.data)
    
# We do a crud of the debtor with a view
class DebtorView(viewsets.ModelViewSet):
    # Create
    def create_debtor(self, request):
        form = DebtorForm(request.POST)
        if form.is_valid():
            form.save()
            return Response(form.data, status=201)
        return Response(form.errors, status=400)
    
    # Read
    def list_debtors(self, request):
        debtors = Debtor.objects.all()
        serializer = DebtorSerializer(debtors, many=True)
        return Response(serializer.data)
    
    def get_debtor_data(self, request, pk):
        debtor = get_object_or_404(Debtor, id=pk)
        serializer = DebtorSerializer(debtor, many=False)
        return Response(serializer.data)
    
    # Update
    def update_debtor_data(self, request, pk):
        debtor = get_object_or_404(Debtor, id=pk)
        serializer = DebtorSerializer(instance=debtor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    # Delete
    def delete_debtor_data(self, request, pk):
        debtor = get_object_or_404(Debtor, id=pk)
        debtor.delete()
        return Response(status=200)
    