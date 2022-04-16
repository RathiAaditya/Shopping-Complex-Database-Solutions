# Generated by Django 4.0.4 on 2022-04-16 14:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0008_remove_company_contact_no_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('Booking_id', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('in_time', models.DateTimeField(auto_now_add=True)),
                ('out_time', models.DateTimeField(auto_now_add=True)),
                ('mobile_no', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(code='no match', message='should be a valid phone number', regex='^(\\+91[\\-\\s]?)?[0]?(91)?[789]\\d{9}$')])),
                ('Invoice_id', models.CharField(max_length=50)),
                ('Slot_no', models.IntegerField()),
            ],
        ),
    ]
