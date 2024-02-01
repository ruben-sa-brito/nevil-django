from django.db import models

class Service(models.Model):
    service_name = models.CharField(max_length=200)
    modify_date = models.DateTimeField("date published")
    oservation = models.TextField(blank=True)
    
    def __str__(self):
        return self.service_name
    
class PriceRange(models.Model):
    small_int = models.IntegerField()
    large_int = models.IntegerField()    
    price = models.FloatField()