from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import Http404
from django.views import generic
from django.http import HttpResponseForbidden
from django.http import HttpResponse


from .models import product
# Create your views here.

teas_pageOne = 1  # first page


def home(request):
    products = product.objects.all()
    newoffers = list(products)
    newoffers.reverse()
    newoffers = newoffers[:4]
    return render(request, 'storeApp/index.html', {
        'products': products,
        'newoffers': newoffers
    })


def search(request):
    return render(request, 'storeApp/search.html')


def userPanel(request):
    return render(request, 'storeApp/userPanel.html')


def userSetting(request):
    return render(request, 'storeApp/userSetting.html')


def accountPanel(request):
    return render(request, 'storeApp/accountPanel.html')


def report(request):
    return render(request, 'storeApp/report.html')


def teas(request):
    return render(request, 'storeApp/teas.html')


def login(request):
    return render(request, 'storeApp/login.html')


def regesiter(request):
    return render(request, 'storeApp/regesiter.html')


def contact(request):
    return render(request, 'storeApp/contact.html')


def checkout(request):
    return render(request, 'storeApp/checkout.html')


def detail(request, pk):
    product_ = get_object_or_404(product,pk=pk)
    newoffers = list(product.objects.all())
    newoffers.reverse()
    newoffers = newoffers[:4]
    return render(request, 'storeApp/detail.html', {
        'product': product_,
        'newoffers': newoffers
        })


def editProduct(request):
    return render(request, 'storeApp/editProduct.html')


def manageOrder(request):
    return render(request, 'storeApp/manageOrder.html')


def manageProductAndDiscount(request):
    return render(request, 'storeApp/manageProductAndDiscount.html')
