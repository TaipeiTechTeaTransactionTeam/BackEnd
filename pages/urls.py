from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.home, name='home'),
    path('userPanel/', views.userPanel, name='userPanel'),
    path('search/', views.search, name='search'),
    path('accountPanel/', views.accountPanel, name='accountPanel'),
]