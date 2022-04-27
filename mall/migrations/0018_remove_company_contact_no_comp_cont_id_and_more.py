# Generated by Django 4.0.4 on 2022-04-26 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0017_remove_company_contact_no_comp_cont_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contracts',
            name='Type',
            field=models.CharField(choices=[('S', 'Selling'), ('R', 'Renting'), ('T', 'Services')], default='R', max_length=1),
        ),
    ]