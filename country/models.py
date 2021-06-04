from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=255, unique=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    code = models.CharField(max_length=3)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.name
