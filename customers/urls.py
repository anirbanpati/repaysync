from django.urls import path
from .views import (
    CustomerListCreateView,
    CustomerCreateView,
    CustomerDetailView,
    BulkCustomerUploadView,
)

urlpatterns = [
    path('', CustomerListCreateView.as_view(), name='customer_list_create'),
    path('create/', CustomerCreateView.as_view(), name='customer_create'),
    path('bulk/upload/', BulkCustomerUploadView.as_view(), name='bulk_customer_upload'),
    path('<int:id>/', CustomerDetailView.as_view(), name='customer_detail'),
]
