# Generated by Django 4.0.4 on 2022-04-26 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0010_contracts_id_alter_contracts_contract_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contracts',
            name='id',
        ),
        migrations.AlterField(
            model_name='contracts',
            name='Contract_id',
            field=models.CharField(max_length=40, primary_key=True, serialize=False),
        ),
    ]