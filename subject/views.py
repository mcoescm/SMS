from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    #return HttpResponse("Hello rohan from subject")
    return render(request,'subject/register.html')
