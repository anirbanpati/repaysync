from django.contrib import admin
from .models import Interaction

@admin.register(Interaction)
class InteractionAdmin(admin.ModelAdmin):
    list_display = ('loan', 'disposition', 'interaction_type', 'timestamp', 'created_by')
    list_filter = ('interaction_type', 'disposition',)
    search_fields = ('loan__loan_account_number', 'comment')
