from django.shortcuts import render

from django.http import HttpResponse
from teacher.models import teacher
from student.models import student
from course.models import course
def index(reqest):
    obj = teacher.objects.get(email="ankushgochke@gmail.com")
    dict = {"data": obj}
    return render(reqest,"attendance/attendance.html", dict)




def findstudents(request):
    obj3 = teacher.objects.get(email="ankushgochke@gmail.com")


    cs = request.POST['crs']
    obj2= course.objects.get(courseid=cs)

    obj = student.objects.all().filter(course_id=cs)
    context = {"students":obj,"cnm" : obj2,"data": obj3}
    return render(request, "attendance/attendance.html", context)

