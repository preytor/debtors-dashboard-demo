from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response

from .models import Payment
from case.models import Case
from .forms import PaymentForm
from .serializer import PaymentSerializer
from .filters import PaymentFilter

from backend_debtors.paginations import CustomPagination

# Create your views here.
# We get a filtered view for the payment
class PaymentViewSet(viewsets.ModelViewSet):

    pagination_class = CustomPagination
    
    def list_payments(self, request, case_id):
        self.filterset_class = PaymentFilter
        case = get_object_or_404(Case, id=case_id)
        queryset = Payment.objects.order_by('id').filter(case=case)
        case = self.request.query_params.get('case', None)
        payment_date = self.request.query_params.get('payment_date', None)
        payment_amount = self.request.query_params.get('payment_amount', None)
        payment_status = self.request.query_params.get('payment_status', None)

        if case is not None:
            queryset = queryset.filter(case=case)
        if payment_date is not None:
            queryset = queryset.filter(payment_date=payment_date)
        if payment_amount is not None:
            queryset = queryset.filter(payment_amount=payment_amount)
        if payment_status is not None:
            queryset = queryset.filter(payment_status=payment_status)

        # Define the number of items per page
        page = self.paginate_queryset(queryset)
        
        if page is not None:
            serializer = PaymentSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = PaymentSerializer(queryset, many=True)
        return Response(serializer.data)

# We do a crud of the payment with a view
class PaymentView(viewsets.ModelViewSet):
    # Create
    def create_payment(self, request):
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return Response(form.data, status=201)
        return Response(form.errors, status=400)
    
    # Read
    def get_payment_data(self, request, pk):
        payment = get_object_or_404(Payment, id=pk)
        serializer = PaymentSerializer(payment, many=False)
        return Response(serializer.data)
    
    # Update
    def update_payment_data(self, request, pk):
        payment = get_object_or_404(Payment, id=pk)
        form = PaymentForm(instance=payment, data=request.data)
        if form.is_valid():
            form.save()
        return Response(form.data)
    
    # Delete
    def delete_payment_data(self, request, pk):
        payment = get_object_or_404(Payment, id=pk)
        payment.delete()
        return Response(status=200)
    