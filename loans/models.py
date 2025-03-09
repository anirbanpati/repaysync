from django.db import models
from customers.models import Customer

# Optional: define loan type choices
LOAN_TYPE_CHOICES = (
    ('personal', 'Personal Loan'),
    ('home', 'Home Loan'),
    ('auto', 'Auto Loan'),
    ('education', 'Education Loan'),
    ('business', 'Business Loan'),
)

class Loan(models.Model):
    loan_account_number = models.CharField(max_length=100, unique=True)
    principal_amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    
    # New fields
    loan_type = models.CharField(
        max_length=50,
        choices=LOAN_TYPE_CHOICES,
        blank=True,
        null=True
    )
    tenure_months = models.PositiveIntegerField(null=True, blank=True)
    loan_date = models.DateField(null=True, blank=True)

    # ForeignKey to associate this loan with a single customer
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='loans'
    )

    class Meta:
        default_permissions = ('add', 'change', 'delete', 'view')

    def __str__(self):
        return f"Loan {self.loan_account_number} - {self.customer.name}"
