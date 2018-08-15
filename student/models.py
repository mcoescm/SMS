from django.db import models
from parent.models import parentreg

# Create your models here.
class studentreg(models.Model):
    fnm = models.CharField(max_length=40)
    mnm = models.CharField(max_length=40)
    lnm = models.CharField(max_length=40)
    parent_id=models.ForeignKey(parentreg, on_delete=models.CASCADE)
    address = models.CharField(max_length=400)
    state = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    pin = models.CharField(max_length=40)
    gender = models.CharField(max_length=40)
    dob = models.DateField()
    age = models.CharField(max_length=3)
    email = models.CharField(max_length=40)
    mobile = models.CharField(max_length=10)
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)