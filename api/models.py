from django.db import models

# Create your models here.
class Plan(models.Model):
    items=models.CharField(max_length=100)
