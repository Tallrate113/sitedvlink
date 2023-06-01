from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import *
from .models import *
from .serializer import ApplicationsSerializer


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

class ApplicationsAPIView(APIView):
    def get(self, request):
        A = Applications.objects.all()
        return Response({'posts': ApplicationsSerializer(A, many=True).data})

    def post(self, request):
        serializer = ApplicationsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk=kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Applications.objects.get(pk=pk)
        except:
            return Response({"error": "Objects does not exists"})

        serializer = ApplicationsSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})


    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})
        try:
            record = Applications.objects.get(pk=pk)
            record.delete()
        except:
            return Response({"error": "Object does not exists"})

        return Response({"post": "delete post " + str(pk)})



