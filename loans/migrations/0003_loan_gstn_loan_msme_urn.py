# Generated by Django 5.1.7 on 2025-03-11 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0002_remove_loan_customer_loan_customers'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='gstn',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='GST Number'),
        ),
        migrations.AddField(
            model_name='loan',
            name='msme_urn',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='MSME Udyam Registration Number'),
        ),
    ]
