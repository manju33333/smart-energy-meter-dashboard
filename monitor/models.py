from django.db import models

# Create your models here.
class EnergyReading(models.Model):
    voltage = models.FloatField()
    current = models.FloatField()
    power = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.voltage}V, {self.current}A, {self.power}W at {self.timestamp}"