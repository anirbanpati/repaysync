from django.contrib.auth.models import AbstractUser
from django.db import models

ROLE_CHOICES = (
    ('collection_officer', 'Collection Officer'),
    ('manager', 'Manager'),
    ('super_manager', 'Super Manager'),
    ('calling_agent', 'Calling Agent'),
)

class CustomUser(AbstractUser):
    role = models.CharField(max_length=30, choices=ROLE_CHOICES)
    manager = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='subordinates'
    )

    class Meta:
      
        default_permissions = ('add', 'change', 'delete', 'view')
    
        permissions = [
            ("can_access_special_feature", "Can Access Special Feature"),
            ("can_view_reports", "Can View Reports"),
        ]

    def __str__(self):
        return self.username
