from django.shortcuts import get_object_or_404

from rest_framework import viewsets, generics
from rest_framework.response import Response

from .models import Case, CaseView
from .forms import CaseForm
from .serializer import CaseSerializer, CaseViewSerializer
from .filters import CaseFilter

from backend_debtors.paginations import CustomPagination

# Create your views here.
# We get a filtered view for the case
class CaseViewSet(generics.ListAPIView):

    queryset = CaseView.objects.all()
    serializer_class = CaseViewSerializer
    pagination_class = CustomPagination
    filter_backends = (CaseFilter,)

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        # Define the number of items per page
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = CaseViewSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = CaseViewSerializer(queryset, many=True)
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
    