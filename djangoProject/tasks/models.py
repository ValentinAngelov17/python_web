from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=30, null=False)
    description = models.TextField()
    priority = models.IntegerField(default=1)
