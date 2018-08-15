from django.db import models
from course.models import course
# Create your models here.

class subject(models.Model):
    subjectid=models.CharField(primary_key=True, max_length=40)
    subjectname=models.CharField(max_length=40)
    courseid=models.ForeignKey(course, on_delete=models.CASCADE)