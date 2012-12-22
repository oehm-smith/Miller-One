from django.db import models

class Store(models.Model):
    name=models.CharField(max_length=64)
    location=models.CharField(max_length=256)
    def __unicode__(self):
        return "%s %s"%(self.name, self.location)
    
class Item(models.Model):
    store=models.ForeignKey(Store)
    name=models.CharField(max_length=64)
    brand=models.CharField(max_length=64)
    cost=models.FloatField()
    datebought=models.DateTimeField('date bought')
    list_per_page=3
    def __unicode__(self):
        return "%s"%(self.name)
