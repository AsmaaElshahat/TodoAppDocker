# Generated by Django 3.1 on 2023-05-11 15:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('postgresConnector', '0004_auto_20230511_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
