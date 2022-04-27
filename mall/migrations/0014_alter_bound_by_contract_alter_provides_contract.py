# Generated by Django 4.0.4 on 2022-04-26 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0013_alter_contracts_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bound_by',
            name='Contract',
            field=models.OneToOneField(default='def', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='mall.contracts'),
        ),
        migrations.AlterField(
            model_name='provides',
            name='Contract',
            field=models.OneToOneField(default='def', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='mall.contracts'),
        ),
    ]