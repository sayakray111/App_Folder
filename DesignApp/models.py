from django.db import models

class User_Details(models.Model):
    Type = models.TextField(default=None)
    Area = models.IntegerField()
    Description = models.CharField(max_length = 120)

class Building_Details(models.Model):
    Area = models.DecimalField(decimal_places=3,max_digits=20)
    #Location here .... 
    Height = models.DecimalField(decimal_places=3, max_digits=20)
    Description = models.CharField(max_length=120)
    


    
