# Generated by Django 4.0.4 on 2022-04-16 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0009_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slots',
            fields=[
                ('Slot_no', models.IntegerField(primary_key=True, serialize=False)),
                ('Slot_status', models.BooleanField(default=False)),
                ('Rate', models.FloatField()),
            ],
        ),
    ]