from django.shortcuts import render, redirect
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .forms import *
from .models import *
from django.contrib.auth.models import *
from .serializer import ApplicationsSerializer


def index(request):
    if request.method == 'POST':
        form = AddAppliForm(request.POST, request.FILES)
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
    if request.method == 'POST':
        form = RegisterUserForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterUserForm()
    context = {'form': form}
    return render(request, 'dvlink/signin.html', context)


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect('account')
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'dvlink/login.html', context)


class ApplicationsViewSet(mixins.CreateModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          mixins.ListModelMixin,
                          GenericViewSet):
    # queryset = Applications.objects.all()
    serializer_class = ApplicationsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        pk = self.kwargs.get("pk")

        if not pk:
            return Applications.objects.all()[:10]

        return Applications.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def stat(self, pk=None):
        stat = Status.objects.get(pk=pk)
        return Response({'stat': stat.name})





