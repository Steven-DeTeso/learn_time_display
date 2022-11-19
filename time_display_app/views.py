from django.shortcuts import render, HttpResponse
from time import gmtime, strftime

# Create your views here.

def index(request):
    return HttpResponse('This is a test to see if its working')

def time(request):
    context = {
        "time": strftime("%A-%b-%-d-%Y %I%M %p", gmtime())
    }
    return render(request, 'index.html', context)