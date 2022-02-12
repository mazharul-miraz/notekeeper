from django.shortcuts import render
from httpx import request

# Create your views here.

def home(requuest):
    return render(request,"index.html")