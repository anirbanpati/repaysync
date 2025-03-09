from django.urls import path
from .views import LoanListCreateView, LoanDetailView

urlpatterns = [
    path('', LoanListCreateView.as_view(), name='loan_list_create'),
    path('<int:id>/', LoanDetailView.as_view(), name='loan_detail'),
]
