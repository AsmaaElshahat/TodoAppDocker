import datetime
from django.db import models
import django.utils.timezone


class Todo(models.Model):
    todo_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    created_at = models.DateTimeField(default=django.utils.timezone.now)
    completed = models.BooleanField(default=False)
    class Meta:
        db_table = "Todo"
