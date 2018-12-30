from django.urls import path

from . import views

app_name = 'storeApp'

urlpatterns = [
    path('', views.home, name='home'),
    path('userPanel/', views.userPanel, name='userPanel'),
    path('userSetting/', views.userSetting, name='userSetting'),
    path('search/', views.search, name='search'),
    path('accountPanel/', views.accountPanel, name='accountPanel'),
    path('teas/', views.teas, name='teas'),
    path('teas/<str:fk>/', views.teas_type, name='teas_type'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('regesiter/', views.regesiter, name='regesiter'),
    path('contact/', views.contact, name='contact'),
    path('checkout/', views.checkout, name='checkout'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('manageOrder/', views.manageOrder, name='manageOrder'),
    path('productQuantity/<str:ids>',views.productQuantity,name="productQuantity"),
    path('product_record',views.product_record,name="product_record"),
]