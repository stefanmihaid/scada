from django.db import models

# Create your models here



class Pole(models.Model):
    SPEEDS = (
        (1, 'LOW'),
	(2, 'MEDIUM'),
        (3, 'HIGH')
    )
    rotationspeed = models.IntegerField(choices=SPEEDS, default=SPEEDS[0][0])
    lightsensor = models.FloatField(default=0.0)
    temperature = models.FloatField(default=0.0)
    soilmoisture = models.FloatField(default=0.0)
	
