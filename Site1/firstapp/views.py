from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    x=[]
    for i in range(10):
        x.append(i)
    return HttpResponse("<h1 Elements are </h1>:List of values {0}".format(x))
