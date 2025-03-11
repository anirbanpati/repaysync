from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Loan
from .serializers import LoanSerializer
from customers.models import Customer

class LoanListCreateView(generics.ListCreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated]

class LoanDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

class CustomerLoanListView(generics.ListAPIView):
    """
    Lists all loans for a specific customer.
    """
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        customer_id = self.kwargs.get('customer_id')
        customer = get_object_or_404(Customer, id=customer_id)
        return customer.loans.all()
