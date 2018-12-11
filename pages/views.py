from django.shortcuts import render,redirect
from django.urls import reverse

# Create your views here.

def home(request):
    return render(request, 'pages/index.html')


def search(request):
    return render(request, 'pages/search.html')