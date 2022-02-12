from django.shortcuts import render
from urllib import request

# Create your views here.

def home(request):
    return render(request,"index.html")


def noteView(request):
    return render(request,"index.html")

def addNote():
    return render(request,"")

def delNote():
    return render(request,"")