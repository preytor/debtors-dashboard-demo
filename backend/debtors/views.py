from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response

from .models import Debtor
from .forms import DebtorForm
from .serializer import DebtorSerializer
from .filters import DebtorFilter

from backend_debtors.paginations import CustomPagination

# Create your views here.
# We get a filtered view for the debtor
class DebtorViewSet(viewsets.ModelViewSet):

    pagination_class = CustomPagination

    def list_debtors(self, request):
        self.filterset_class = DebtorFilter
        queryset = Debtor.objects.all()
        name = self.request.query_params.get('name', None)
        initial_debt = self.request.query_params.get('initial_debt', None)
        legal_status = self.request.query_params.get('legal_status', None)

        if name is not None:
            queryset = queryset.filter(name=name)
        if initial_debt is not None:
            queryset = queryset.filter(initial_debt=initial_debt)
        if legal_status is not None:
            queryset = queryset.filter(legal_status=legal_status)

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
        form = DebtorForm(request.POST, instance=debtor)
        if form.is_valid():
            form.save()
        return Response(form.data)
    
    # Delete
    def delete_debtor_data(self, request, pk):
        debtor = get_object_or_404(Debtor, id=pk)
        debtor.delete()
        return Response(status=200)
    