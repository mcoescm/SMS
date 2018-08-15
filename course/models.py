from django.db import models

# Create your models here.


class department(models.Model):
    deptname = models.CharField(primary_key=True, max_length=40)


class course(models.Model):
    courseid=models.CharField(primary_key=True, max_length=40)
    coursename=models.CharField(unique= True, max_length=40)
    dept=models.ForeignKey(department, on_delete=models.CASCADE)
