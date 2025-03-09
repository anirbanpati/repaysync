from django.contrib import admin
from .models import APILog

@admin.register(APILog)
class APILogAdmin(admin.ModelAdmin):
    list_display = ('method', 'endpoint', 'status_code', 'user', 'created_at')
    list_filter = ('method', 'status_code', 'created_at')
    search_fields = ('endpoint', 'request_payload', 'response_payload')
