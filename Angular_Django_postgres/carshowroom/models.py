from django.db import models


class Cars(models.Model):
    carbrand=models.CharField(max_length=30,default="",blank=False)
    cartype=models.CharField(max_length=30)
    avilable=models.BooleanField(default=True)

