# Generated by Django 4.2.1 on 2023-05-16 14:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('postgresConnector', '0006_alter_todo_todo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]