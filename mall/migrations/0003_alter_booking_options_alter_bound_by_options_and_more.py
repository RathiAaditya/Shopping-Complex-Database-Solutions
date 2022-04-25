# Generated by Django 4.0.4 on 2022-04-25 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0002_alter_contracts_type_alter_customer_mobile_id_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'verbose_name_plural': 'Bookings'},
        ),
        migrations.AlterModelOptions(
            name='bound_by',
            options={'verbose_name_plural': 'Bound_by'},
        ),
        migrations.AlterModelOptions(
            name='companies',
            options={'verbose_name_plural': 'Companies'},
        ),
        migrations.AlterModelOptions(
            name='contracts',
            options={'verbose_name_plural': 'Contracts'},
        ),
        migrations.AlterModelOptions(
            name='invoice',
            options={'verbose_name_plural': 'Invoices'},
        ),
        migrations.AlterModelOptions(
            name='provides',
            options={'verbose_name_plural': 'Provides'},
        ),
        migrations.AlterModelOptions(
            name='services',
            options={'verbose_name_plural': 'Services'},
        ),
        migrations.AlterModelOptions(
            name='shops',
            options={'verbose_name_plural': 'Shops'},
        ),
        migrations.AlterModelOptions(
            name='slots',
            options={'verbose_name_plural': 'Slots'},
        ),
        migrations.AlterField(
            model_name='contracts',
            name='Company',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mall.companies'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='Date_issued',
            field=models.DateTimeField(),
        ),
    ]
