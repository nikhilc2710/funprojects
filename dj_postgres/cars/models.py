from django.db import models

# Create your models here.
class Driver(models.Model):
    name=models.TextField()
    license=models.TextField()
    

class Car(models.Model):
    carname=models.TextField()
    carType=models.TextField()
    purchased=models.DateField()
    owner=models.ForeignKey("Driver",on_delete=models.SET_NULL,null=True)

