# Generated by Django 4.0.4 on 2022-04-25 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0004_invoice_totalamount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='TotalAmount',
        ),
    ]