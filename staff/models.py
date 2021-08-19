from django.db import models

# Create your models here.
class vehicle(models.Model):
    vehicle_name = models.CharField(max_length=16)
    vehicle_type = models.CharField(max_length=64)