from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Interaction
from .serializers import InteractionSerializer
from .permissions import IsFieldOfficer, IsCallingAgent
import pandas as pd

"""
Interaction Endpoints:

Field Interaction Endpoints:
  - FieldInteractionCreateView: Create a field interaction.
  - FieldInteractionDetailView: Retrieve, update, or delete a specific field interaction.
  - FieldInteractionListView: List all field interactions for a given loan.
  
Calling Interaction Endpoints:
  - CallingInteractionCreateView: Create a calling interaction.
  - CallingInteractionDetailView: Retrieve, update, or delete a specific calling interaction.
  - CallingInteractionListView: List all calling interactions for a given loan.
  
BulkInteractionUploadView:
  - Upload multiple interaction records via CSV.
"""

# ---------- Field Interaction Endpoints ----------
class FieldInteractionCreateView(generics.CreateAPIView):
    queryset = Interaction.objects.all()
    serializer_class = InteractionSerializer
    permission_classes = [IsAuthenticated, IsFieldOfficer]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, interaction_type='field')

class FieldInteractionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InteractionSerializer
    permission_classes = [IsAuthenticated, IsFieldOfficer]
    lookup_field = 'id'

    def get_queryset(self):
        return Interaction.objects.filter(interaction_type='field')

class FieldInteractionListView(generics.ListAPIView):
    serializer_class = InteractionSerializer
    permission_classes = [IsAuthenticated, IsFieldOfficer]

    def get_queryset(self):
        # Expecting a URL parameter 'loan_id'
        loan_id = self.kwargs.get('loan_id')
        return Interaction.objects.filter(interaction_type='field', loan__id=loan_id).order_by('-timestamp')

# ---------- Calling Interaction Endpoints ----------
class CallingInteractionCreateView(generics.CreateAPIView):
    queryset = Interaction.objects.all()
    serializer_class = InteractionSerializer
    permission_classes = [IsAuthenticated, IsCallingAgent]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, interaction_type='calling')

class CallingInteractionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InteractionSerializer
    permission_classes = [IsAuthenticated, IsCallingAgent]
    lookup_field = 'id'

    def get_queryset(self):
        return Interaction.objects.filter(interaction_type='calling')

class CallingInteractionListView(generics.ListAPIView):
    serializer_class = InteractionSerializer
    permission_classes = [IsAuthenticated, IsCallingAgent]

    def get_queryset(self):
        # Expecting a URL parameter 'loan_id'
        loan_id = self.kwargs.get('loan_id')
        return Interaction.objects.filter(interaction_type='calling', loan__id=loan_id).order_by('-timestamp')

# ---------- Bulk Upload Endpoint (Shared) ----------
class BulkInteractionUploadView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

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
                    interaction_data = {
                        'loan': row['loan_id'],  # CSV must include a 'loan_id' column
                        'comment': row['comment'],
                        'disposition': row['disposition'],
                        'next_call_date': row.get('next_call_date', None),
                        'interaction_type': row.get('interaction_type', 'field'),
                    }
                    serializer = InteractionSerializer(data=interaction_data)
                    if serializer.is_valid():
                        serializer.save(created_by=request.user)
                        records_created += 1
                    else:
                        errors.append({'row': index, 'errors': serializer.errors})
                except Exception as e:
                    errors.append({'row': index, 'error': str(e)})
            return Response({'records_created': records_created, 'errors': errors})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
