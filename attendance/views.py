from django.shortcuts import render
from teacher.models import teacher
from student.models import studentreg
def index(reqest):
    obj = teacher.objects.get(email="ankushgochke@gmail.com")
    dict = {"data": obj}
    return render(reqest,"attendance/attendance.html", dict)



def retrieve(request):
    dept = request.POST['dept']
    course = request.POST['crs']

