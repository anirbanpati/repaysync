from django.db import migrations
import uuid

def populate_customer_code(apps, schema_editor):
    Customer = apps.get_model('customers', 'Customer')
    for customer in Customer.objects.filter(customer_code__isnull=True):
        customer.customer_code = uuid.uuid4().hex[:8].upper()
        customer.save(update_fields=['customer_code'])

class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_customer_code),
    ]
