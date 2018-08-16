from django.db import models
from parent.models import parent
from course.models import department,course

# Create your models here.
class student(models.Model):
    fnm = models.CharField(max_length=40)
    mnm = models.CharField(max_length=40)
    lnm = models.CharField(max_length=40)
    parent_id = models.ForeignKey(parent, on_delete=models.CASCADE)
    address = models.CharField(max_length=400)
    state = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    pin = models.CharField(max_length=40)
    gender = models.CharField(max_length=40)
    dob = models.DateField()
    mobile = models.CharField(max_length=10)
    dept=models.ForeignKey(department, null=True, on_delete=models.SET_NULL)
    course_id=models.ForeignKey(course, null=True, on_delete=models.SET_NULL)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=40)