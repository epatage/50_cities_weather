from django.db import models


class City(models.Model):
    name = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )
    country = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )
    lat = models.FloatField(
        null=True,
        blank=True,
    )
    lon = models.FloatField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.name}"
