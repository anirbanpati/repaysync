from django.db import models
from customers.models import Customer
from django.core.exceptions import ValidationError

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
    
    # GSTN and MSME URN fields
    gstn = models.CharField(max_length=15, blank=True, null=True, verbose_name="GST Number")
    msme_urn = models.CharField(max_length=16, blank=True, null=True, verbose_name="MSME Udyam Registration Number")

    # Replace ForeignKey with ManyToManyField to allow multiple customers
    customers = models.ManyToManyField(
        Customer,
        related_name='loans'
    )

    class Meta:
        default_permissions = ('add', 'change', 'delete', 'view')

    def __str__(self):
        customers_str = ", ".join([customer.name for customer in self.customers.all()[:3]])
        return f"Loan {self.loan_account_number} - {customers_str}"
    
    def clean(self):
        # Validate that there are no more than 3 customers per loan
        if self.pk and self.customers.count() > 3:
            raise ValidationError("A loan cannot have more than 3 customers.")
        super().clean()
    
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
