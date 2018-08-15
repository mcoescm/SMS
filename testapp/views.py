from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("testapp")

def getdata(request):
    render(request, 'testapp/getdata.html')