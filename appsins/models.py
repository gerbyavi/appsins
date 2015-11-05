from django.db import models

# Create your models here.

class Item(models.Model):
    datt= models.DateField()
    asin = models.CharField(max_length=10,default='')
    rank = models.IntegerField(default=0)
    name= models.TextField(default='')
    cmpt = models.IntegerField(default=0)
    nfl = models.IntegerField(default=0)
    calc = models.DecimalField(max_digits=5, decimal_places=2,default=0.00)
    minprice = models.DecimalField(max_digits=5, decimal_places=2,default=0.00)
    minpriceful = models.DecimalField(max_digits=5, decimal_places=2,default=0.00)
    cost = models.DecimalField(max_digits=5, decimal_places=2,default=0.00)
    clcminuscost = models.DecimalField(max_digits=5, decimal_places=2,default=0.00)
    precentprof = models.DecimalField(max_digits=5, decimal_places=2,default=0.00)
