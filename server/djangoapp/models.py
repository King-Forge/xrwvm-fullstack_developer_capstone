# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

BODY_TYPES = [
    ('SUV', 'SUV'),
    ('Sedan', 'Sedan'),
    ('Hatchback', 'Hatchback'),
    ('Coupe', 'Coupe'),
    ('Convertible', 'Convertible'),
    ('Minivan', 'Minivan'),
    ('Pickup', 'Pickup'),
]

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    # Other fields as needed

    def __str__(self):
        return self.name  # Return the name as the string representation

class CarModel(models.Model):
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length = 20, choices=BODY_TYPES)
    year = models.IntegerField(validators=[MinValueValidator(2015), MaxValueValidator(now().year)])

    def __str__(self):
        return self.name  # Return the name as the string representation