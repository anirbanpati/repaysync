from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'customer_code',
        'name',
        'phone',
        'email',
        'assigned_collection_officer',
        'city',
        'pincode',
    )
    search_fields = ('customer_code', 'name', 'phone', 'email')
    readonly_fields = ('customer_code',)
    # Do not include customer_code in fields since it's non-editable.
    fields = (
        'name',
        'phone',
        'email',
        'assigned_collection_officer',
        'address_line_1',
        'address_line_2',
        'city',
        'state',
        'pincode',
        'date_of_birth',
    )
