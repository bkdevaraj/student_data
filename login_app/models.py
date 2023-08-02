
from django.db import models

class User(models.Model):
    # Define your fields here
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=128)
    # Add more fields as needed

    # Add any methods or custom logic for the model

# Create your models here.
