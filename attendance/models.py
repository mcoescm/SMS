
from django.db import models
from course.models import course


class test(models.Model):
    sid = models.IntegerField(12)
    ispresent = models.IntegerField(12, default=0)
    ccid = models.ForeignKey(course,on_delete=models.CASCADE, null=True)
    dt = models.CharField(max_length=40)

