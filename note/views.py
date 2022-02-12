from django.shortcuts import render
from urllib import request
from .models import noteModel

# Create your views here.

def home(request):
    all_notes_items = noteModel.objects.all()
    return render(request,"index.html",{'all_notes':all_notes_items})


def noteView(request):
    return render(request,"index.html")

def addNote():
    return render(request,"")

def delNote():
    return render(request,"")