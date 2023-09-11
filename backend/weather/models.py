
from django.db import models
from cities.models import City


class Weather(models.Model):
    """Погода."""

    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name='weather_set',
    )
    dt = models.IntegerField(
        null=False,
        blank=False,
    )
    temp = models.FloatField(
        null=False,
        blank=False,
    )
    pressure = models.IntegerField(
        null=True,
        blank=True,
    )
    humidity = models.IntegerField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.city} - {self.dt} - {self.temp}(C)"
