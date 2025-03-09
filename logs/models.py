from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class APILog(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    method = models.CharField(max_length=10)
    endpoint = models.CharField(max_length=255)
    request_payload = models.TextField(blank=True, null=True)
    response_payload = models.TextField(blank=True, null=True)
    status_code = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        default_permissions = ('add', 'change', 'delete', 'view')
        # custom permissions can go here if needed

    def __str__(self):
        return f"{self.method} {self.endpoint} ({self.status_code})"
