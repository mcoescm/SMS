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
    occ= request.POST['occupation']
    contact = request.POST['contact']
    email = request.POST['email']
    password = request.POST['password']
    obj=parent()
    obj.fnm=fnm
    obj.mnm=mnm
    obj.lnm=lnm
    obj.address=address
    obj.state=state
    obj.city=city
    obj.pin=pin
    obj.gender=gender
    obj.dob=dob
    obj.city=city
    obj.occ=occ
    obj.phno=contact
    obj.pwd=password
    obj.email=email
    obj.save()
    return HttpResponse("Success")


def updateparent(request):
    return render(request,"parent/update.html")


def update(request):
    mail = request.POST['hiden']
    obj = parent.objects.filter(email=mail)

    dict = {"data": obj}
    return render(request, "parent/updateparent.html", dict)


def finalupdate(request):
    fnm = request.POST['fname']
    mnm = request.POST['mname']
    lnm = request.POST['lname']
    address = request.POST['addr']
    state = request.POST['state']
    city = request.POST['city']
    pin = request.POST['pin']
    gender = request.POST['get']
    dob = request.POST['dob']
    occ = request.POST['occupation']
    contact = request.POST['contact']
    email = request.POST['email']
    password = request.POST['password']
    id = request.POST['hide']
    # subject.objects.filter(pk=sid).update(subjectname = subjectnm,courseid_id=cid)
    parent.objects.filter(pk=id).update(fnm=fnm,mnm=mnm,lnm=lnm,address=address,state=state,city=city,pin=pin,gender=gender,
                                        dob=dob,occ=occ,phno=contact,email=email,pwd=password)
    return HttpResponse("Saved")




















