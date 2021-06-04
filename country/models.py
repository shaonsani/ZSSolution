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


class State(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='state')

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.name


class Address(models.Model):
    name = models.CharField(max_length=255, unique=True)
    house_number = models.CharField(max_length=255)
    road_number = models.IntegerField()
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='address')

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.name
