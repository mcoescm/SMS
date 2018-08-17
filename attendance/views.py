from django.shortcuts import render

from django.http import HttpResponse
from teacher.models import teacher
from student.models import student
from course.models import course
from .models import test

def index(request):
    em = request.session['user']
    obj = teacher.objects.get(email= em)
    dict = {"data": obj}
    return render(request,"attendance/attendance.html",dict)




def findstudents(request):
    em = request.session['user']
    obj3 = teacher.objects.get(email=em)


    cs = request.POST['crs']
    obj2= course.objects.get(courseid=cs)

    obj = student.objects.all().filter(course_id=cs)
    context = {"students":obj,"cnm" : obj2,"data": obj3}
    return render(request, "attendance/attendance.html", context)

def store (request):
    css = request.GET.get('ccid')
    cdt = request.GET.get('dt')
    obj = student.objects.all().filter(course_id=css)

    dict = {"Sid": obj}

    list=request.GET.getlist("att")



    for i in obj:
        obj2 = test()
        obj2.sid = i.id
        obj2.ccid_id = css
        obj2.dt = cdt
        obj2.save()

    var = ""

    for i in list:
        test.objects.filter(sid = i).update(ispresent=1)


