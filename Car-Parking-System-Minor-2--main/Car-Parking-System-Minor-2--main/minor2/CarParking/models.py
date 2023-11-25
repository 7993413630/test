from django.db import models

class CarParkingSpace(models.Model):
    area = models.CharField(max_length=100)
    total_spaces = models.IntegerField()
    available_spaces = models.IntegerField()
