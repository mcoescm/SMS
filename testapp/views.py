from django.shortcuts import render
from django.http import HttpResponse
from course.models import course
# Create your views here.
def index(request):
    #return HttpResponse("testapp")
    return render(request, 'testapp/getdata.html')


def geta(request):
    cid=request.POST["courseid"]
    obj=course.objects.get(courseid=cid);
    return HttpResponse(obj.coursename)