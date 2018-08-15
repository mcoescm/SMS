from django.shortcuts import render
from django.http import HttpResponse
from course.models import course
from subject.models import subject
# Create your views here.
def index(request):
    #return HttpResponse("Hello rohan from subject")
    obj=course()
    obj=course.objects.all();
    dict={"dept":obj}
    return render(request, 'subject/register.html', dict)
    #return render(request,'subject/register.html')

def register(request):
    subid=request.POST["subid"]
    subname=request.POST["subnm"]
    cnm=request.POST["coursename"]
    obj=subject()
    obj2=course()
    obj2.courseid=course.objects.get(coursename=cnm)
    obj.subjectid=subid
    obj.subjectname=subname
    obj.courseid_id=obj2.courseid
    obj.save()
    return HttpResponse("success")


































































