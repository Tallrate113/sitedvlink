from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'dvlink/index.html',{'title':'Главная страница'})

def account(request):
    return render(request, 'dvlink/account.html',{'title':'Аккаунт'})
