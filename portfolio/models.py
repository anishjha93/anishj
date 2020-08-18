from django.db import models

# Create your models here.

class Work(models.Model):
    designation = models.CharField(max_length=30)
    company_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    projects = models.CharField(max_length= 100)
    duration = modes.CharField(max_length=100)
