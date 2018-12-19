from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.home, name='home'),
    path('userPanel/', views.userPanel, name='userPanel'),
    path('search/', views.search, name='search'),
    path('accountPanel/', views.accountPanel, name='accountPanel'),
    path('report/', views.report, name='report'),
    path('teas/', views.teas, name='teas'),
    path('login/', views.login, name='login'),
    path('regesiter/', views.regesiter, name='regesiter'),
    path('contact/', views.contact, name='contact'),
    path('checkout/', views.checkout, name='checkout'),
    path('detail/', views.detail, name='detail'),
    path('blacktea/', views.blacktea, name='blacktea'),
    path('greentea/', views.greentea, name='greentea'),
    path('oolong/', views.oolong, name='oolong'),
    path('teas/', views.teas, name='teas')
]