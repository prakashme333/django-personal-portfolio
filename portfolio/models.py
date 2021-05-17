from django.db import models


# Create your models here.

class Project(models.Model):
   title = models.CharField(max_length=100,blank=True)
   description= models.CharField(max_length=250)
   image = models.ImageField(upload_to='portfolio/images/',blank=True, height_field=None, width_field=None, max_length=None)
   url = models.URLField(blank=True)
   
   def __str__(self):
      return self.title 