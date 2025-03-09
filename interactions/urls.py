from django.urls import path
from .views import (
    FieldInteractionCreateView,
    FieldInteractionDetailView,
    FieldInteractionListView,
    CallingInteractionCreateView,
    CallingInteractionDetailView,
    CallingInteractionListView,
    BulkInteractionUploadView,
)

urlpatterns = [
    # Field interaction endpoints
    path('field/create/', FieldInteractionCreateView.as_view(), name='field_interaction_create'),
    path('field/<int:id>/', FieldInteractionDetailView.as_view(), name='field_interaction_detail'),
    path('field/loan/<int:loan_id>/', FieldInteractionListView.as_view(), name='field_interaction_list'),

    # Calling interaction endpoints
    path('calling/create/', CallingInteractionCreateView.as_view(), name='calling_interaction_create'),
    path('calling/<int:id>/', CallingInteractionDetailView.as_view(), name='calling_interaction_detail'),
    path('calling/loan/<int:loan_id>/', CallingInteractionListView.as_view(), name='calling_interaction_list'),

    # Bulk upload endpoint (shared)
    path('bulk/upload/', BulkInteractionUploadView.as_view(), name='bulk_interaction_upload'),
]
