from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def studreg(request):
    return render(request, "student/studentreg.html")


def studsave(request):
    return HttpResponse("Form submitted successfully...")
