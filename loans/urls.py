# loans/urls.py
from django.urls import path
from .views import (
    LoanListCreateView,
    LoanDetailView,
    CustomerLoanListView,  # <-- new view
)

urlpatterns = [
    path('', LoanListCreateView.as_view(), name='loan_list_create'),
    path('<int:id>/', LoanDetailView.as_view(), name='loan_detail'),
    path('customer/<int:customer_id>/', CustomerLoanListView.as_view(), name='customer_loans_list'),
]
