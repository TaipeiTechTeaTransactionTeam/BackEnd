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

def teas(request):
    return render(request,'pages/teas.html')

def login(request):
    return render(request,'pages/login.html')

def regesiter(request):
    return render(request,'pages/regesiter.html')

def contact(request):
    return render(request, 'pages/contact.html')

def checkout(request):
    return render(request, 'pages/checkout.html')

def detail(request):
    return render(request, 'pages/detail.html')

def blacktea(request):
    return render(request, 'pages/teas')

def greentea(request):
    return render(request, 'pages/teas')

def oolong(request):
    return render(request, 'pages/teas')