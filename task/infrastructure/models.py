from django.db import models


class Task(models.Model):
    name=models.CharField(verbose_name="name",max_length=30,unique=True)
    details=models.CharField(verbose_name="details",max_length=1000)


    