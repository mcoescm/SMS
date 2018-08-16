from django.shortcuts import render
from django.http import HttpResponse
from student.models import student
from parent.models import parent

# Create your views here.

def studreg(request):
    return render(request, "student/register.html")


def studsave(request):
    btn = request.POST['s']
    if btn == "parent":
        sfnm = request.POST['sfname']
        smnm = request.POST['smname']
        slnm = request.POST['slname']
        data = parent.objects.filter(lnm=slnm)
        context = {'fname': sfnm, 'mname': smnm, 'lname': slnm, 'pdata': data}
        return render(request,'student/register.html', context)
    else:
        #Getting Data
        sfnm = request.POST['sfname']
        smnm = request.POST['smname']
        slnm = request.POST['slname']

        pfn=request.POST['ffname']
        pmn=request.POST['fmname']
        pln=request.POST['flname']
        dad=parent.objects.get(fnm=pfn,mnm=pmn,lnm=pln)
        address = request.POST['addr']
        state = request.POST['state']
        city = request.POST['city']
        pin = request.POST['pin']
        gender = request.POST['get']
        dob = request.POST['dob']
        contact = request.POST['contact']
        email = request.POST['email']
        password = request.POST['password']

        # Saving Data
        obj=student()
        obj.fnm = sfnm
        obj.mnm = smnm
        obj.lnm = slnm
        obj.parent_id_id = dad.id
        obj.address = address
        obj.state = state
        obj.city = city
        obj.pin = pin
        obj.gender = gender
        obj.dob = dob
        obj.phno = contact
        obj.email = email
        obj.pwd = password
        obj.save()
        return HttpResponse("Parent " + "" + pfn + " " + dad.lnm + "<br>Student is " + sfnm)








def getData(request):

    btn = request.POST['aaa']
    name=request.POST['name']
    parent="hello"
    if btn == "Get1":
        context = {'data': name,'par': parent}
        return render(request, 'student/test.html', context)
    elif btn == "Get2":
        data = ["ankush Gochke"]
        context = {'data': data}
        return render(request, 'student/test.html', context)
