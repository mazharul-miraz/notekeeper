from django.http import HttpResponseRedirect
from django.shortcuts import render
from urllib import request
from .models import noteModel
from .form import noteForm
# Create your views here.

def home(request):
    all_notes_items = noteModel.objects.all()
    return render(request,"index.html",{'all_notes':all_notes_items})


#add form data here
def addNote(request):
    if request.method == 'POST':
        form = noteForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form= noteForm()
    return HttpResponseRedirect('/')


def delNote():
    return render(request,"")