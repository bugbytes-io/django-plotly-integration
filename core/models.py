from django.db import models

# Create your models here.
class CO2(models.Model):
    date = models.DateField()
    average = models.FloatField()

    class Meta:
        ordering = ('date',)
