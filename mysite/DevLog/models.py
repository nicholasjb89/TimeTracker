from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Log(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    hours = models.FloatField(default=0.0)
    date_time = models.DateTimeField("date published")
    comment = models.CharField(max_length=500)

    def __str__(self):
        return self.comment
