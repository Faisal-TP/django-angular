from django.db import models

# Create your models here.

class Userregister(models.Model):
    f_name=models.CharField(max_length=30)
    l_name=models.CharField(max_length=30)
    dob=models.CharField(max_length=30)
    gender=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
