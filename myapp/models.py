from django.db import models

# Create your models here.
from django.db import models


class MyData(models.Model):
    sid = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    datetime = models.DateTimeField(max_length=255,null=True, blank=True)
    longitude = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.CharField(max_length=255, null=True, blank=True)
    elevation = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name='form'