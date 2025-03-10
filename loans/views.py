from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Loan
from .serializers import LoanSerializer

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
        return Loan.objects.filter(customer_id=customer_id)
