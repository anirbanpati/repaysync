from django.db import models
from loans.models import Loan
from users.models import CustomUser

INTERACTION_TYPE_CHOICES = (
    ('field', 'Field'),
    ('calling', 'Calling'),
)

DISPOSITION_CHOICES = (
    ('called', 'Called'),
    ('visited', 'Visited'),
    ('promise_to_pay', 'Promise to Pay'),
)

class Interaction(models.Model):
    # Allow loan to be nullable and blank, so existing records don't need a default.
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, related_name='interactions', null=True, blank=True)
    comment = models.TextField()
    disposition = models.CharField(max_length=50, choices=DISPOSITION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    next_call_date = models.DateField(null=True, blank=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    interaction_type = models.CharField(max_length=50, choices=INTERACTION_TYPE_CHOICES, default='field')

    class Meta:
        default_permissions = ('add', 'change', 'delete', 'view')

    def __str__(self):
        loan_info = self.loan.loan_account_number if self.loan else 'N/A'
        return f"Interaction for Loan {loan_info} at {self.timestamp}"
