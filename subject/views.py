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
    temp=course.objects.get(coursename=cnm)
    obj2.courseid=temp.courseid
    obj.subjectid=subid
    obj.subjectname=subname
    obj.courseid_id=obj2.courseid
    obj.save()
    return HttpResponse("success")

def updatesubject(request):
    return render(request,"subject/update.html")

def update(request):
    subnm = request.POST['hiden']
    obj = subject.objects.filter(subjectname=subnm)
    obj2 = course.objects.all()
    dict = {"data": obj, "alldata": obj2}

    return render(request, "subject/updatesubject.html", dict)


def finalupdate(request):
    subjectnm=request.POST['snm']
    sid=request.POST['sid']
    cid=request.POST['selectcourse']


    subject.objects.filter(pk=sid).update(subjectname = subjectnm,courseid_id=cid)
    return HttpResponse("success")






























































