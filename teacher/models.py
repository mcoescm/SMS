from django.db import models
from course.models import course
from subject.models import subject
from course.models import department


# Create your models here.
class teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    isadmin=models.CharField(max_length=10)
    firstname=models.CharField(max_length=40)
    middlename=models.CharField(max_length=40)
    lastname=models.CharField(max_length=40)
    address=models.CharField(max_length=400)
    state=models.CharField(max_length=40)
    city=models.CharField(max_length=40)
    pin=models.CharField(max_length=40)
    gender=models.CharField(max_length=40)
    dob=models.DateField()
    contact=models.CharField(max_length=40)
    password=models.CharField(max_length=40)
    email=models.CharField(unique=True, max_length=40)
    dept=models.ForeignKey(department, on_delete=models.CASCADE)
    course_id=models.ForeignKey(course, on_delete=models.CASCADE)
    subject=models.ForeignKey(subject, on_delete=models.CASCADE)


class examschedule(models.Model):
    course=models.ForeignKey(course, null=True, on_delete=models.SET_NULL)
    subject=models.ForeignKey(subject,null=True,on_delete=models.SET_NULL)
    examdate=models.DateField()
    timefrom=models.TimeField()
    timeto=models.TimeField()

