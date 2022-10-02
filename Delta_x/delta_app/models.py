from django.db import models


class Data(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    season = models.CharField(max_length=20)
    latitude = models.FloatField()
    longitude = models.FloatField()
    date = models.DateTimeField()
    time = models.TimeField()
    turbidity = models.FloatField()
    salinity = models.FloatField()
    temperature = models.FloatField()
