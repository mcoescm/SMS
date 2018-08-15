from django.shortcuts import render
from django.http import HttpResponse
from parent.models import parent
# Create your views here.

def index(request):
    return render(request, "parent/register.html")


def register(request):
    fnm=request.POST['fname']
    mnm = request.POST['mname']
    lnm = request.POST['lname']
    address=request.POST['addr']
    state=request.POST['state']
    city = request.POST['city']
    pin = request.POST['pin']
    gender = request.POST['get']
    dob = request.POST['dob']
    ages = request.POST['ages']
    occ= request.POST['occupation']
    contact = request.POST['contact']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    obj=parent()
    obj.fnm=fnm
    obj.mnm=mnm
    obj.lnm=lnm
    obj.address=address
    obj.state=state
    obj.city=state
    obj.pin=pin
    obj.gender=gender
    obj.dob=dob
    obj.age=ages
    obj.occ=occ
    obj.phno=contact
    obj.unm=username
    obj.pwd=password
    obj.email=email
    obj.save()
    return HttpResponse("Success")


























