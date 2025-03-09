from django.contrib import admin
from .models import Loan

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = (
        'loan_account_number',
        'customer',
        'loan_type',
        'tenure_months',
        'loan_date',
        'principal_amount',
        'interest_rate',
    )
    search_fields = ('loan_account_number', 'customer__name')
    fields = (
        'loan_account_number',
        'customer',
        'loan_type',
        'principal_amount',
        'interest_rate',
        'tenure_months',
        'loan_date',
    )
