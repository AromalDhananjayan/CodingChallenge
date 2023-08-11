from django.db import models

# Create your models here.

class City(models.Model):
    Cityname = models.CharField(max_length=200)
    Citycode = models.IntegerField()

    def __str__(self):
        return f"{self.Cityname} {self.Citycode}"

class Country(models.Model):
    Countryname = models.CharField(max_length=200)
    Countrycode = models.IntegerField()

    def __str__(self):
        return self.Countryname 