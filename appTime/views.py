from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, localtime, strftime 
# Create your views here.
def index (request):
    fecha = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime()),
        "localTime": strftime("%Y-%m-%d %H:%M %p", localtime())
    }
    print("*"*50)
    print(fecha)
    return render(request,"index.html",{"time":fecha["time"],"localTime":fecha["localTime"]})