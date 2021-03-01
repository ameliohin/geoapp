from django.db import models
from location_field.models.spatial import LocationField
from django.contrib.gis.geos import Point


class Branch(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True)
    location = LocationField(default=Point(51.60431839178197,46.115950578823686))

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    position_title =  models.CharField(max_length=128, blank=True, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
