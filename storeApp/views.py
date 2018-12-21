from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import Http404
from django.views import generic
from django.http import HttpResponseForbidden
from django.http import HttpResponse
from django.forms.models import modelform_factory
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required


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
    if request.user.is_authenticated:
        return render(request, 'storeApp/userPanel.html')
    else:
        return render(request, 'storeApp/login.html')


def userSetting(request):
    return render(request, 'storeApp/userSetting.html')


def accountPanel(request):
    return render(request, 'storeApp/accountPanel.html')


def report(request):
    return render(request, 'storeApp/report.html')


def teas(request):
    return render(request, 'storeApp/teas.html')


@require_http_methods(['POST', 'GET'])
def login(request):
    # LoginForm = modelform_factory(User, fields=('username', 'password'))
    if request.method == 'POST':
        name = request.POST['username']  # 取得表單傳送的帳號、密碼
        password = request.POST['password']
        user = auth.authenticate(username=name, password=password)  # 使用者驗證
        if user is not None:  # 若驗證成功，以 auth.login(request,user) 登入
            if user.is_active:
                auth.login(request, user)
                message = '登入成功!'
                # 登入成功產生一個 Session，重導到<index.html>
                return redirect('storeApp:home')
            else:
                message = '帳號尚未啟用!'
        else:
            message = '登入失敗!'
            return render(request, 'storeApp/login.html', locals())
    return render(request, 'storeApp/login.html', locals())


@login_required
def logout(request):
    auth.logout(request)  # 登出成功清除 Session，重導到<index.html>
    return redirect('storeApp:home')


@require_http_methods(['POST', 'GET'])
def regesiter(request):
    if request.method == 'POST':
        data = request.POST
        try:
            user = User.objects.get(username=data['username'])
        except:
            user = None  # 若 username 不存在則設定為 None
        if user != None:
            message = user.username + " 帳號已經建立! "
            return render(request, 'storeApp/regesiter.html', {'message': message})
        else:  # 建立 username 帳號
            user = User.objects.create_user(
                data['username'], data['email'], data['password'])
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.is_staff = "False"
            user.save()  # 將資料寫入資料庫
            # 若成功建立，重新導向至 index.html
            return redirect('storeApp:home')
    else:
        return render(request, 'storeApp/regesiter.html')


def contact(request):
    return render(request, 'storeApp/contact.html')


def checkout(request):
    return render(request, 'storeApp/checkout.html')


def detail(request, pk):
    product_ = get_object_or_404(product, pk=pk)
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
