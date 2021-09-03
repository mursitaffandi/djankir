from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.
class vehicle(models.Model):
    vehicle_name = models.CharField(max_length=16)
    vehicle_wheels = models.PositiveIntegerField(default=2, validators=[MinValueValidator(1), MaxValueValidator(16)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)