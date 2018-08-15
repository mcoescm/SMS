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
