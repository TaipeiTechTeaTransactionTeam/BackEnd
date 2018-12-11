from django.shortcuts import render,redirect
from django.urls import reverse

# Create your views here.

def home(request):
    return render(request, 'pages/index.html')


def search(request):
    return render(request, 'pages/search.html')

def userPanel(request):
    return render(request, 'pages/userPanel.html')

def accountPanel(request):
    return render(request,'pages/accountPanel.html')
def report(request):
    return render(request,'pages/report.html')