from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response

from .models import Case
from debtors.models import Debtor
from worker.models import Worker
from .forms import CaseForm
from .serializer import CaseSerializer
from .filters import CaseFilter

from backend_debtors.paginations import CustomPagination

# Create your views here.
# We get a filtered view for the case
class CaseViewSet(viewsets.ModelViewSet):

    pagination_class = CustomPagination

    def list_cases(self, request):
        self.filterset_class = CaseFilter
        queryset = Case.objects.order_by('id').all()
        debtor = self.request.query_params.get('debtor', None)
        assigned_worker = self.request.query_params.get('assigned_worker', None)
        case_status = self.request.query_params.get('case_status', None)

        if debtor is not None:
            queryset = queryset.filter(debtor=debtor)
        if assigned_worker is not None:
            queryset = queryset.filter(assigned_worker=assigned_worker)
        if case_status is not None:
            queryset = queryset.filter(case_status=case_status)

        # Define the number of items per page
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = CaseSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = CaseSerializer(queryset, many=True)
        return Response(serializer.data)
    
# We do a crud of the case with a view
class CaseView(viewsets.ModelViewSet):
    # Create
    def create_case(self, request):
        form = CaseForm(request.POST)
        if form.is_valid():
            form.save()
        return Response(form.data, status=201)
    
    # Read
    def get_case_data(self, request, pk):
        case = get_object_or_404(Case, id=pk)
        serializer = CaseSerializer(case, many=False)
        return Response(serializer.data)
    
    # Update
    def update_case_data(self, request, pk):
        case = get_object_or_404(Case, id=pk)
        serializer = CaseSerializer(instance=case, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
    # Delete
    def delete_case_data(self, request, pk):
        case = get_object_or_404(Case, id=pk)
        case.delete()
        return Response(status=200)
    