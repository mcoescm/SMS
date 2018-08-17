from django.shortcuts import render
from django.http import HttpResponse
from student.models import student
from parent.models import parent
from teacher.models import teacher

# Create your views here.

def index (request):
    return render(request, "login/login.html")

def checklogin(request):
    cuser = request.POST['user']
    unm = request.POST['username']
    pwd = request.POST['password']


    if cuser=='teacher':
        obj = teacher.objects.get(email = unm)
        if obj.isadmin == "YES":
            return HttpResponse("Admin !")
        else:
            return HttpResponse("Teacher !")

    elif cuser == 'student':
        return HttpResponse("Student !")

    elif cuser == "parent":
        return HttpResponse("Parent")
