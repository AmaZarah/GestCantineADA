from django.db import models

# Create your models here.

class MenuMolel(models.Model):
    plat = models.OneToOneField('plat.PlatModel', on_delete=models.CASCADE)
    creat_dat = models.DateField(auto_now_add=True)
      
