from django.shortcuts import render,redirect
from django.urls import reverse

# Create your views here.

teas_pageOne = 1 # first page

def home(request):
    return render(request, 'storeApp/index.html')

def search(request):
    return render(request, 'storeApp/search.html')

def userPanel(request):
    return render(request, 'storeApp/userPanel.html')

def accountPanel(request):
    return render(request,'storeApp/accountPanel.html')
    
def report(request):
    return render(request,'storeApp/report.html')

def teas(request):
    return render(request,'storeApp/teas.html')

def login(request):
    return render(request,'storeApp/login.html')

def regesiter(request):
    return render(request,'storeApp/regesiter.html')

def contact(request):
    return render(request, 'storeApp/contact.html')
