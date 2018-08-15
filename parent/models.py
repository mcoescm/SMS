from django.db import models

# Create your models here.



class parentreg(models.Model):
    fnm = models.CharField(max_length=40)
    mnm = models.CharField(max_length=40)
    lnm = models.CharField(max_length=40)
    address = models.CharField(max_length=400)
    state = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    pin = models.CharField(max_length=40)
    gender = models.CharField(max_length=40)
    dob = models.DateField()
    age = models.CharField(max_length=3)
    occ = models.CharField(max_length=40)
    phno = models.CharField(max_length=10)
    unm = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    pwd = models.CharField(max_length=40)
