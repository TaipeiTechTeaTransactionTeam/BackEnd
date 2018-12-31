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
import json
import math
from pprint import pprint
from .models import *
from .productDiscountItem import ProductDiscountItem, getProductDiscountList

# Create your views here.

teas_pageOne = 1  # first page


def home(request):
    types = TeaType.objects.all()
    newoffers = list(Product.objects.all())
    newoffers.reverse()
    newoffers = newoffers[:4]
    products = getProductDiscountList(newoffers)
    return render(request, 'storeApp/index.html', locals())


def search(request):
    types = TeaType.objects.all()
    if request.method == 'POST':
        search_text = request.POST['Search']
        products = Product.objects.filter(name__contains=search_text)
        page = 1
        total_page = math.ceil(len(products) / 9)
        # 計算上、下頁
        previous_page = page - 1
        next_page = page + 1 if total_page >= page + 1 else 0
        total_page = range(1, total_page+1)
        products = getProductDiscountList(
            list(products)[(page - 1) * 9:page * 9])
        return render(request, 'storeApp/search.html', locals())
    elif request.method == 'GET':
        if 'page' in request.GET and 'quireText' in request.GET:
            search_text = request.GET['quireText']
            if request.GET['page'] == '':
                page = 1
            else:
                page = int(request.GET['page'])
        else:
            page = 1
        # 取出總頁數
        products = Product.objects.filter(name__contains=search_text)
        total_page = math.ceil(len(products) / 9)
        # 計算上、下頁
        previous_page = page - 1
        next_page = page + 1 if total_page >= page + 1 else 0
        # 變成可迭代物件
        total_page = range(1, total_page+1)
        # 取好 9 個商品
        products = getProductDiscountList(
            list(products)[(page - 1) * 9:page * 9])
        return render(request, 'storeApp/search.html', locals())


def userPanel(request):
    if request.user.is_authenticated:
        types = TeaType.objects.all()
        # 取得目前使用者的訂單
        orders = Order.objects.filter(own_user=request.user)
        #
        order_contain_products = OrderContainProduct.objects.all()
        order_list = []
        for order in orders:
            order_list.append(
                {'order_id': order.id, 'items': order_contain_products.filter(order=order)})
        return render(request, 'storeApp/userPanel.html', locals())
    else:
        return redirect('storeApp:login')


def userSetting(request):
    types = TeaType.objects.all()
    return render(request, 'storeApp/userSetting.html', locals())


def accountPanel(request):
    types = TeaType.objects.all()
    return render(request, 'storeApp/accountPanel.html', locals())


def productQuantity(request, ids):
    ans = []
    try:
        if ids[0] != "[":
            id = int(ids)
            ans = float(Product.objects.get(pk=id).amount)
        else:
            ids = json.loads(ids)
            ans = [float(x.amount)
                   for x in list(Product.objects.filter(id__in=ids).all())]
        return HttpResponse(json.dumps(ans))
    except:
        return HttpResponse(-1)


def teas(request):
    types = TeaType.objects.all()
    teas = Product.objects.all()
    if 'page' in request.GET:
        if request.GET['page'] == '':
            page = 1
        else:
            page = int(request.GET['page'])
    else:
        page = 1
    # 取出總頁數
    total_page = math.ceil(len(teas) / 9)
    # 計算上、下頁
    previous_page = page - 1
    next_page = page + 1 if total_page >= page + 1 else 0
    # 變成可迭代物件
    total_page = range(1, total_page+1)
    # 取好 9 個商品
    teas = getProductDiscountList(list(teas)[(page - 1) * 9:page * 9])

    return render(request, 'storeApp/teas.html', locals())


def teas_type(request, fk):
    麵包屑 = fk
    types = TeaType.objects.all()
    products = Product.objects.all()
    teas = products.filter(tea_type=types.get(name=fk))
    if 'page' in request.GET:
        if request.GET['page'] == '':
            page = 1
        else:
            page = int(request.GET['page'])
    else:
        page = 1
    # 取出總頁數
    total_page = math.ceil(len(teas) / 9)
    # 計算上、下頁
    previous_page = page - 1
    next_page = page + 1 if total_page >= page + 1 else 0
    # 變成可迭代物件
    total_page = range(1, total_page+1)
    # 取好 9 個商品
    teas = getProductDiscountList(list(teas)[(page - 1) * 9:page * 9])
    return render(request, 'storeApp/teas.html', locals())


def manageOrder(request):
    types = TeaType.objects.all()
    orders = Order.objects.filter(own_user=request.user)
    oneOrder = []
    for i in reversed(orders):
        oneOrder.append(
            {'order': i, 'products': OrderContainProduct.objects.filter(order=i)})
    return render(request, 'storeApp/manageOrder.html', locals())


@require_http_methods(['POST', 'GET'])
def login(request):
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
    types = TeaType.objects.all()
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
                username=data['username'], password=data['password'])
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.is_staff = "False"
            user.save()  # 將資料寫入資料庫
            # 若成功建立，重新導向至 index.html
            return redirect("storeApp:home")
    else:
        return render(request, 'storeApp/regesiter.html', locals())


def contact(request):
    types = TeaType.objects.all()
    return render(request, 'storeApp/contact.html', locals())


def checkout(request):
    # 茶類型
    types = TeaType.objects.all()
    # 運費
    shippingPrice = list(Store.objects.all())[0].freight
    # 運費折扣
    try:
        shippingDiscount = [x for x in list(
            ShippingDiscount.objects.all()) if x.isValidNow()][-1]
    except:
        shippingDiscount = None

    if request.method == 'GET':
        # 事件折扣
        eventDiscounts = [x for x in list(
            SeasoningDiscount.objects.all()) if x.isValidNow()]
        return render(request, 'storeApp/checkout.html', locals())

    elif request.method == 'POST':
        # 登入驗證
        if not request.user.is_authenticated:
            return redirect('storeApp:login')
        # 初始化總價
        total_price = 0
        # 解析收到的資料
        datas = json.loads(request.POST['items'])
        
        # 計算原總價
        for data in datas:
            total_price += Product.objects.get(
                id=data['uid']).get_discount_price()['price'] * data['quantity']
        #print("總價",total_price)
        try:
            # 拿出所選的折扣
            eventDiscount = SeasoningDiscount.objects.get(
                id=json.loads(request.POST.get("eventDiscount", ''))["id"])
        except:
            eventDiscount = None

        if eventDiscount and eventDiscount.isValidNow():
            # 折價券折扣計算後的值
            total_price -= eventDiscount.discountValue(total_price)

        if shippingDiscount and shippingDiscount.isValidNow():
            # 運費折扣後
            total_price = shippingDiscount.calculate_price(
                total_price, shippingPrice)

        order = Order(own_user=request.user, total_price=total_price)
        order.save()

        for data in datas:
            product = Product.objects.get(id=data['uid'])
            OrderContainProduct.objects.create(
                order=order, product=product, purchase_quantity=data['quantity'])
            product.amount -= data['quantity']
            product.save()

    return render(request, 'storeApp/checkout.html', locals())


def detail(request, pk):
    types = TeaType.objects.all()
    product_ = get_object_or_404(Product, pk=pk)
    product = getProductDiscountList([product_])[0]
    newoffers = list(Product.objects.all())
    newoffers.reverse()
    products = getProductDiscountList(newoffers[:4])
    return render(request, 'storeApp/detail.html', locals())


def product_record(request):
    types = TeaType.objects.all()
    orders = Order.objects.filter(own_user=request.user)
    ids = []
    for i in orders:
        for j in OrderContainProduct.objects.filter(order=i):
            ids.append(j.product.id)
    products = Product.objects.filter(id__in=ids)
    return render(request, 'storeApp/product_record.html', locals())
