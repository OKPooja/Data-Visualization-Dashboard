from django.db import models

# Create your models here.
class Data(models.Model):
    end_year = models.CharField(max_length= 10)
    intensity = models.CharField(max_length= 10)
    sector = models.CharField(max_length= 256)
    topic = models.CharField(max_length= 256)
    insight = models.CharField(max_length= 256)
    url = models.CharField(max_length= 1000)
    region = models.CharField(max_length= 256)
    start_year = models.CharField(max_length= 10) 
    impact = models.CharField(max_length= 10)
    added = models.CharField(max_length= 100)
    published = models.CharField(max_length= 100)
    country = models.CharField(max_length= 256)
    relevance = models.CharField(max_length= 10)
    pestle = models.CharField(max_length= 256)
    source = models.CharField(max_length= 256)
    title = models.CharField(max_length= 256)
    likelihood = models.CharField(max_length= 10)
    
