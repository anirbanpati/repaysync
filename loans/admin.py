from django.contrib import admin
from .models import Loan

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = (
        'loan_account_number',
        'get_customers',
        'loan_type',
        'tenure_months',
        'loan_date',
        'principal_amount',
        'interest_rate',
        'gstn',
        'msme_urn',
    )
    search_fields = ('loan_account_number', 'customers__name', 'gstn', 'msme_urn')
    filter_horizontal = ('customers',)
    fields = (
        'loan_account_number',
        'customers',
        'loan_type',
        'principal_amount',
        'interest_rate',
        'tenure_months',
        'loan_date',
        'gstn',
        'msme_urn',
    )
    
    def get_customers(self, obj):
        return ", ".join([customer.name for customer in obj.customers.all()[:3]])
    get_customers.short_description = 'Customers'
