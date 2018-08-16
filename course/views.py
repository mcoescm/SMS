from django.shortcuts import render
from django.http import HttpResponse
from .models import course , department
# Create your views here.
def index(request):
    #return HttpResponse("Hello rohan from course")
    return render(request, 'course/register.html')

def registercourse(request):
    courseid=request.POST['cid']
    coursename = request.POST['cnm']
    deptid= request.POST['dnm']

    obj2 = department()
    obj2.deptname = deptid

    obj=course()
    obj.courseid=courseid
    obj.coursename=coursename
    obj.dept_id= obj2.deptname
    try:
        obj.save()
        return HttpResponse("saved")
    except:
        return HttpResponse()


def updatecourse(request):
    return render(request, "course/update.html")

def update(request):
    coursenm=request.POST['hiden']
    obj=course.objects.filter(coursename=coursenm)
    obj2 = department.objects.all()
    dict={"data":obj,"alldata":obj2}

    return render(request , "course/updatecourse.html", dict )

def updatecoursefinal(request):
    coursenm=request.POST['cnm']
    cid=request.POST['cid']
    did=request.POST['selectdept']

    #obj=course.objects.get(pk=oldcid)
    course.objects.filter(pk=cid).update(coursename=coursenm, courseid=cid, dept_id=did)
    return HttpResponse("success")
