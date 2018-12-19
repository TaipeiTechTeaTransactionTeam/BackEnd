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

def userSetting(request):
    return render(request, 'storeApp/userSetting.html')

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

def checkout(request):
    return render(request, 'storeApp/checkout.html')

def detail(request):
    return render(request, 'storeApp/detail.html')

def editProduct(request):
    return render(request, 'storeApp/editProduct.html')

def manageOrder(request):
    return render(request, 'storeApp/manageOrder.html')

def manageProductAndDiscount(request):
    return render(request, 'storeApp/manageProductAndDiscount.html')