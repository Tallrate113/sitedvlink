from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import *
from .models import *
def index(request):
    if request.method == 'POST':
        form = AddAppliForm(request.POST)
        if form.is_valid():
            try:
                Applications.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка в создании заявки')
    else:
        form = AddAppliForm()
    return render(request, 'dvlink/index.html', {'form': form, 'title': 'Главная страница'})

def account(request):
    posts = Applications.objects.all()
    return render(request, 'dvlink/account.html', {'posts': posts, 'title': 'Аккаунт'})

def signin(request):
    posts = Applications.objects.all()
    return render(request, 'dvlink/signinpage.html', {'posts': posts, 'title': 'Регистрация'})
