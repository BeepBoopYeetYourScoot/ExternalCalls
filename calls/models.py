from django.db import models

# Create your models here.


class Farm(models.Model):

    name = models.CharField(max_length=25)
    location = models.CharField(max_length=25)
    capacity = models.IntegerField()
    buy_price = models.IntegerField()

    def __str__(self):
        return self.name
