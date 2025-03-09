from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
import pandas as pd

from .models import Customer
from .serializers import CustomerSerializer
from .permissions import IsCustomerAccessible

class CustomerListCreateView(generics.ListCreateAPIView):
    """
    GET: Lists customers.
         - Both calling agents and field collectors see only customers assigned to them.
    POST: Creates a new customer.
         - The current user is automatically set as the assigned_collection_officer.
    """
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Customer.objects.filter(assigned_collection_officer=user)

class CustomerCreateView(generics.CreateAPIView):
    """
    Dedicated endpoint for creating a single customer.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve a specific customer's details.
    PUT/PATCH: Update customer information.
    DELETE: Remove a customer.
    Uses custom permission 'IsCustomerAccessible'.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated, IsCustomerAccessible]
    lookup_field = 'id'

class BulkCustomerUploadView(generics.GenericAPIView):
    """
    Endpoint for bulk uploading customers via CSV.
    
    Expected CSV columns:
      - customer_code (optional, if not provided, auto-generation will occur),
      - name,
      - phone,
      - email,
      - address_line_1,
      - address_line_2,
      - city,
      - state,
      - pincode,
      - date_of_birth (format: YYYY-MM-DD)
    
    Automatically assigns the current user as the assigned_collection_officer.
    """
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        file_obj = request.FILES.get('file')
        if not file_obj:
            return Response({'error': 'No file provided.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            df = pd.read_csv(file_obj)
            records_created = 0
            errors = []
            for index, row in df.iterrows():
                try:
                    customer_data = {
                        # If customer_code is not provided, the model default will auto-generate one.
                        'customer_code': row.get('customer_code', None),
                        'name': row['name'],
                        'phone': row.get('phone', ''),
                        'email': row.get('email', ''),
                        'assigned_collection_officer': request.user.id,
                        'address_line_1': row.get('address_line_1', ''),
                        'address_line_2': row.get('address_line_2', ''),
                        'city': row.get('city', ''),
                        'state': row.get('state', ''),
                        'pincode': row.get('pincode', ''),
                        'date_of_birth': row.get('date_of_birth', None),
                    }
                    serializer = CustomerSerializer(data=customer_data)
                    if serializer.is_valid():
                        serializer.save()
                        records_created += 1
                    else:
                        errors.append({'row': index, 'errors': serializer.errors})
                except Exception as e:
                    errors.append({'row': index, 'error': str(e)})
            return Response({'records_created': records_created, 'errors': errors})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
