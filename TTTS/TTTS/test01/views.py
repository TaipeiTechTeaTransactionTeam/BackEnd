from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.s
def sayHelloWorld(request):
    #return HttpResponse("hello django!")
    return render(request,'home.html')