from django.db import models

# Create your models here.


class Vehicle(models.Model):
    
    name = models.CharField(max_length=200) 
    speed = models.FloatField(default=40, max_length=3)
    avg_speed = models.FloatField(default=40, max_length=3)
    temperature = models.FloatField(default=40, max_length=3)
    fuel_level = models.IntegerField(default=60)
    engine_status = models.CharField(max_length=200 , default="OK")
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    ignition = models.BooleanField(default=False) #on or off

    logo = models.ImageField(upload_to="base/logo" , default="")
    camera1 = models.ImageField(upload_to="base/camera1" , default="")
    camera2 = models.ImageField(upload_to="base/camera2" , default="")
    static_map = models.ImageField(upload_to="base/static_map" , default="")

    def __str__(self):
        return f"{self.name} - {self.ignition}"
