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


from .models import product, teaType
# Create your views here.

teas_pageOne = 1  # first page


def home(request):
    types = teaType.objects.all()
    products = product.objects.all()
    newoffers = list(products)
    newoffers.reverse()
    newoffers = newoffers[:4]
    return render(request, 'storeApp/index.html', {
        'products': products,
        'newoffers': newoffers,
        'types': types
    })


def search(request):
    types = teaType.objects.all()
    return render(request, 'storeApp/search.html', locals())


def userPanel(request):
    if request.user.is_authenticated:
        types = teaType.objects.all()
        return render(request, 'storeApp/userPanel.html', locals())
    else:
        return render(request, 'storeApp/login.html')


def userSetting(request):
    types = teaType.objects.all()
    return render(request, 'storeApp/userSetting.html', locals())


def accountPanel(request):
    types = teaType.objects.all()
    return render(request, 'storeApp/accountPanel.html', locals())


def report(request):
    types = teaType.objects.all()
    return render(request, 'storeApp/report.html', locals())


def teas(request):
    types = teaType.objects.all()
    teas = product.objects.all()
    return render(request, 'storeApp/teas.html', locals())


def teas_type(request, fk):
    types = teaType.objects.all()
    products = product.objects.all()
    teas = products.filter(teaType=types.get(name=fk))
    return render(request, 'storeApp/teas.html', locals())


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
    types = teaType.objects.all()
    if request.method == 'POST':
        data = request.POST
        try:
            user = User.objects.get(username=data['username'])
        except:
            user = None  # 若 username 不存在則設定為 None
        if user != None:
            message = user.username + " 帳號已經建立! "
            return render(request, 'storeApp/regesiter.html', locals())
        else:  # 建立 username 帳號
            user = User.objects.create_user(
                data['username'], data['email'], data['password'])
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.is_staff = "False"
            shoppingCart = shoppingCart(ownUser = user)
            user.save()  # 將資料寫入資料庫
            shoppingCart.save()
            # 若成功建立，重新導向至 index.html
            return redirect('storeApp:`home`')
    else:
        return render(request, 'storeApp/regesiter.html', locals())


def contact(request):
    types = teaType.objects.all()
    return render(request, 'storeApp/contact.html', locals())


def checkout(request):
    types = teaType.objects.all()
    return render(request, 'storeApp/checkout.html', locals())


def detail(request, pk):
    types = teaType.objects.all()
    product_ = get_object_or_404(product, pk=pk)
    newoffers = list(product.objects.all())
    newoffers.reverse()
    newoffers = newoffers[:4]
    return render(request, 'storeApp/detail.html', {
        'product': product_,
        'newoffers': newoffers,
        'types': types
    })


def editProduct(request):
    types = teaType.objects.all()
    return render(request, 'storeApp/editProduct.html', locals())


def manageOrder(request):
    types = teaType.objects.all()
    return render(request, 'storeApp/manageOrder.html', locals())


def manageProductAndDiscount(request):
    types = teaType.objects.all()
    return render(request, 'storeApp/manageProductAndDiscount.html', locals())
