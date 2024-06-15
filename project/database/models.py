from django.db import models

# Create your models here.

class Persons(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(default='default@example.com') # Add default value
    address = models.CharField(max_length=255, default='Unknown address')
    city = models.CharField(max_length=100, default='Unknown city')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"