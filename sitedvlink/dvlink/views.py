from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import generics, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

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
    def stat(self, request, pk=None):
        stat = Status.objects.get(pk=pk)
        return Response({'stat': stat.name})



# class ApplicationsAPIList(generics.ListCreateAPIView):
#     queryset = Applications.objects.all()
#     serializer_class = ApplicationsSerializer
#
# class ApplicationsAPIUpdate(generics.UpdateAPIView):
#     queryset = Applications.objects.all()
#     serializer_class = ApplicationsSerializer
#
# class ApplicationsAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Applications.objects.all()
#     serializer_class = ApplicationsSerializer




