# Generated by Django 4.0.4 on 2022-04-25 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0003_alter_booking_options_alter_bound_by_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='TotalAmount',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]