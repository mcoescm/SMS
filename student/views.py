from django.shortcuts import render
from django.http import HttpResponse
from student.models import student
from parent.models import parent
from course.models import department,course

# Create your views here.

def studreg(request):
    return render(request, "student/register.html")

def studupdate(request):
    return render(request, "student/update.html")



def studsave(request):
    btn = request.POST['s']
    if btn == "parent":
        sfnm = request.POST['sfname']
        smnm = request.POST['smname']
        slnm = request.POST['slname']
        data = parent.objects.filter(lnm=slnm)
        dp = department.objects.all()
        crs = course.objects.all()
        context = {'fname': sfnm, 'mname': smnm, 'lname': slnm, 'pdata': data, 'dept':dp, 'course':crs}
        return render(request,'student/register.html', context)
    else:
        #Getting Data
        sfnm = request.POST['sfname']
        smnm = request.POST['smname']
        slnm = request.POST['slname']

        pfn=request.POST['ffname']
        pmn=request.POST['fmname']
        pln=request.POST['flname']
        dp=request.POST['dept']
        crs=request.POST['course']
        dad=parent.objects.get(fnm=pfn,mnm=pmn,lnm=pln)
        dt=department.objects.get(deptname=dp)
        cour=course.objects.get(coursename=crs)
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
        obj.dept_id=dt.deptname
        obj.course_id_id=cour.courseid
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



def update(request):
    btn=request.POST['submit']

    if btn == "Get":
        mail = request.POST['studemail']
        obj = student.objects.filter(email=mail)
        obj1 = student.objects.get(email=mail)
        dp = department.objects.all()
        crs = course.objects.filter(dept=obj1.dept_id)
        context = {"data": obj,'course':crs}
        return render(request, "student/update.html", context)
        #return HttpResponse("Email is "+mail)

    else :
        fnm = request.POST['fname']
        mnm = request.POST['mname']
        lnm = request.POST['lname']
        address = request.POST['addr']
        state = request.POST['state']
        city = request.POST['city']
        pin = request.POST['pin']
        gender = request.POST['get']
        dob = request.POST['dob']
        contact = request.POST['contact']
        email = request.POST['email']
        password = request.POST['password']
        id = request.POST['hide']
        # subject.objects.filter(pk=sid).update(subjectname = subjectnm,courseid_id=cid)
        student.objects.filter(pk=id).update(fnm=fnm, mnm=mnm, lnm=lnm, address=address, state=state, city=city, pin=pin,
                                            gender=gender,
                                            dob=dob, phno=contact, email=email, pwd=password)
        return HttpResponse("Saved")

        return HttpResponse("Hello")




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
