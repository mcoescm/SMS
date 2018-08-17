from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from teacher.models import teacher

# Create your views here.

def index (request):
    return render(request, "login/login.html")

def checklogin(request):
    cuser = request.POST['user']
    unm = request.POST['username']
    pwd = request.POST['password']
    request.session['user'] = unm

    if cuser=='teacher':
        obj = teacher.objects.get(email = unm)
        if obj.isadmin == "YES":
               return HttpResponseRedirect("/teacher/")
        else:
            return render(request, "attendance/attendance.html")

    elif cuser == 'student':
        return HttpResponse("Student !")

    elif cuser == "parent":
        return HttpResponse("Parent")
