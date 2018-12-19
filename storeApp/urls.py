from django.urls import path

from . import views

app_name = 'storeApp'

urlpatterns = [
    path('', views.home, name='home'),
    path('userPanel/', views.userPanel, name='userPanel'),
    path('userSetting/', views.userSetting, name='userSetting'),
    path('search/', views.search, name='search'),
    path('accountPanel/', views.accountPanel, name='accountPanel'),
    path('report/', views.report, name='report'),
    path('teas/', views.teas, name='teas'),
    path('login/', views.login, name='login'),
    path('regesiter/', views.regesiter, name='regesiter'),
    path('contact/', views.contact, name='contact'),
    path('checkout/', views.checkout, name='checkout'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('editProduct/', views.editProduct, name='editProduct'),
    path('manageOrder/', views.manageOrder, name='manageOrder'),
    path('manageProductAndDiscount/', views.manageProductAndDiscount, name='manageProductAndDiscount'),
]