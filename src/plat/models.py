from django.db import models

# Create your models here.


class PlatModel(models.Model):
    name = models.CharField( max_length=50)
    summury = models.CharField(max_length=30)
