from django.shortcuts import render
from django.http import HttpResponse
from course.models import course, department
from subject.models import subject
from subject.models import subject
from teacher.models import teacher,examschedule


# Create your views here.
def index(request):
    deptobj=department.objects.all()
    courseobj=course.objects.all()
    subobj=subject.objects.all()
    dict={"dept":deptobj , "course":courseobj, "subject":subobj}
    return render(request, "teacher/register.html",dict)

def update(request):
    deptobj = department.objects.all()
    courseobj = course.objects.all()
    subobj = subject.objects.all()
    context = {"dept": deptobj, "course": courseobj, "subject": subobj}
    return render(request, "teacher/update.html", context)

"""
def setdata(request):
    deptobj=department.objects.all()
    courseobj=course.objects.all()
    subobj=subject.objects.all()
    dict={"dept":deptobj , "course":courseobj, "subject":subobj}
    return render(request, "teacher/register.html",dict)
"""

def register(request):
    fnm=request.POST['fname']
    mnm=request.POST['mname']
    lnm=request.POST['lname']
    addres=request.POST['addr']
    stat=request.POST['state']
    cit=request.POST['city']
    pn=request.POST['pin']
    gend=request.POST['get']
    bdate=request.POST['dob']
    cont=request.POST['contact']
    eml=request.POST['email']
    pwd=request.POST['password']
    depid=request.POST['dept']
    cid=request.POST['course']
    sub=request.POST['subject']
    admin=request.POST['role']
    obj=teacher()
    deptobj=department()
    courseobj=course()
    subjectobj=subject()
    deptobj.deptname=depid
    temp=course.objects.get(coursename=cid)
    temp1=department.objects.get(deptname=depid)
    temp2=subject.objects.get(subjectname=sub)
    subjectobj.subjectid=sub
    obj.firstname=fnm
    obj.middlename=mnm
    obj.lastname=lnm
    obj.state=stat
    obj.city=cit
    obj.pin=pn
    obj.password=pwd
    obj.email=eml
    obj.gender=gend
    obj.contact=cont
    obj.dept_id=temp1.deptname
    obj.subject_id=temp2.subjectid
    obj.course_id_id=temp.courseid
    obj.isadmin=admin
    obj.address=addres
    obj.dob=bdate
    obj.save()
    return HttpResponse("success")


def updation(request):
    btn = request.POST['submit']

    if btn == "Get":
        mail = request.POST['studemail']
        obj = teacher.objects.filter(email=mail)
        #context = {"data": obj}
        deptobj = department.objects.all()
        courseobj = course.objects.all()
        subobj = subject.objects.all()
        context = {"dept": deptobj, "course": courseobj, "subject": subobj, "data": obj}
        return render(request, "teacher/update.html", context)
    else:
        dp = request.POST['dept']
        cr = request.POST['course']
        su = request.POST['subject']
        dt = department.objects.get(deptname=dp)
        cour = course.objects.get(coursename=cr)
        sub = subject.objects.get(subjectname=su)
        admin = request.POST['role']
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
        teacher.objects.filter(pk=id).update(firstname=fnm, middlename=mnm, lastname=lnm, address=address, state=state,
                                             city=city, pin=pin,
                                             gender=gender, isadmin=admin, dob=dob, contact=contact, email=email,
                                             password=password, dept_id=dt.deptname, course_id_id=cour.courseid,
                                             subject_id=sub.subjectid)
        return HttpResponse("<h3>" + fnm + " Your updation is successfully done....</h3>")


def exams(request):
    deptobj=department.objects.all()
    courseobj=course.objects.all()
    dict={"department":deptobj, "course":courseobj}

    return render(request, "teacher/exam_schedule.html", dict)


def findsubject(request):
    cid=request.POST['course']
    obj=course.objects.get(coursename=cid)
    subjectobj=subject.objects.all().filter(courseid=obj.courseid)
    dict={"subjectname":subjectobj, "coursedata":obj.coursename}
    return render(request,"teacher/exam_schedule.html", dict)



def schedule(request):
    cour = request.GET.getlist('crs')
    sub = request.GET.getlist('subject')
    dt = request.GET.getlist('date')
    frm = request.GET.getlist('from')
    to = request.GET.getlist('to')


    var=""

    for i in range(0,len(sub)) :
        exam = examschedule()
        cor = course.objects.all().get(coursename=cour[i])
        sb = subject.objects.all().get(subjectname=sub[i])
        exam.course_id = cor.courseid
        exam.subject_id = sb.subjectid
        exam.examdate = dt[i]
        exam.timefrom = frm[i]
        exam.timeto = to[i]
        exam.save()

        var+=" "+cour[i] +"  "+sub[i]+"  "+dt[i]+"<br> "

    return HttpResponse(var)
    '''
    for (c,s,d,f,t) in zip(cour,sub,dt,frm,to) :
        obj=examschedule()
        cor=course.objects.all().get(coursename=c)
        sb=subject.objects.all().get(subjectname=s)
        obj.course_id= cor.courseid
        obj.subject_id=sb.subjectid
        obj.examdate=d
        obj.timefrom=f
        obj.timeto=t
        obj.save()'''


