# Generated by Django 5.1.7 on 2025-03-09 17:01

import customers.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_code', models.CharField(default=customers.models.generate_customer_code, editable=False, max_length=100, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address_line_1', models.CharField(blank=True, max_length=255, null=True)),
                ('address_line_2', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, choices=[('AN', 'Andaman and Nicobar Islands'), ('AP', 'Andhra Pradesh'), ('AR', 'Arunachal Pradesh'), ('AS', 'Assam'), ('BR', 'Bihar'), ('CH', 'Chandigarh'), ('CT', 'Chhattisgarh'), ('DN', 'Dadra and Nagar Haveli and Daman and Diu'), ('DL', 'Delhi'), ('GA', 'Goa'), ('GJ', 'Gujarat'), ('HR', 'Haryana'), ('HP', 'Himachal Pradesh'), ('JK', 'Jammu and Kashmir'), ('JH', 'Jharkhand'), ('KA', 'Karnataka'), ('KL', 'Kerala'), ('LA', 'Ladakh'), ('LD', 'Lakshadweep'), ('MP', 'Madhya Pradesh'), ('MH', 'Maharashtra'), ('MN', 'Manipur'), ('ML', 'Meghalaya'), ('MZ', 'Mizoram'), ('NL', 'Nagaland'), ('OR', 'Odisha'), ('PY', 'Puducherry'), ('PB', 'Punjab'), ('RJ', 'Rajasthan'), ('SK', 'Sikkim'), ('TN', 'Tamil Nadu'), ('TG', 'Telangana'), ('TR', 'Tripura'), ('UP', 'Uttar Pradesh'), ('UT', 'Uttarakhand'), ('WB', 'West Bengal')], max_length=100, null=True)),
                ('pincode', models.CharField(blank=True, max_length=20, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('assigned_collection_officer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_permissions': ('add', 'change', 'delete', 'view'),
            },
        ),
    ]
