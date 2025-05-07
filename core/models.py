from django.db import models

class Exercise(models.Model):
    date        = models.DateField()
    distance_km = models.DecimalField(max_digits=5, decimal_places=2)
    time_min    = models.PositiveIntegerField()

    @property
    def pace(self):
        return float(self.time_min) / float(self.distance_km)

    def __str__(self):
        return f"{self.date} – {self.distance_km} km en {self.time_min} min"
