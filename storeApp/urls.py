from django.urls import path

from . import views

app_name = 'storeApp'

urlpatterns = [
    path('', views.home, name='home'),
    path('user_panel/', views.user_panel, name='user_panel'),
    path('user_setting/', views.user_setting, name='user_setting'),
    path('user_setting/edit_password/', views.edit_password, name='edit_password'),
    path('search/', views.search, name='search'),
    path('account_panel/', views.account_panel, name='account_panel'),
    path('teas/', views.teas, name='teas'),
    path('teas/<str:fk>/', views.teas_type, name='teas_type'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('regesiter/', views.regesiter, name='regesiter'),
    path('contact/', views.contact, name='contact'),
    path('checkout/', views.checkout, name='checkout'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('order_list/', views.order_list, name='order_list'),
    path('order_detail/<int:pk>/', views.order_detail, name='order_detail'),
    path('productQuantity/<str:ids>',views.productQuantity,name="productQuantity"),
    path('product_record',views.product_record,name="product_record"),
    path('forgot_password/', views.forgot_password, name='forgot_password'),    
]