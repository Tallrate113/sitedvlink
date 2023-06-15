from django.contrib.auth import authenticate, logout
from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
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
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        form = AddAppliAccForm(request.POST, profile=profile)
        if form.is_valid():
            application = form.save(commit=False)
            application.field_organisation_name = profile.organisation_name
            application.field_email = request.user.email
            application.field_number_phone = profile.number_phone
            application.field_fio = request.user.username
            application.stat_id = 1
            application.user = request.user
            application.save()
            return redirect('account')
    else:
        form = AddAppliAccForm(profile=profile)

    posts = Applications.objects.filter(user=request.user)
    return render(request, 'dvlink/account.html', {'form': form, 'posts': posts, 'title': 'Аккаунт'})


# def signin(request):
#     if request.method == 'POST':
#         form = RegisterUserForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = RegisterUserForm()
#     context = {'form': form}
#     return render(request, 'dvlink/signin.html', context)

def signin(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        p_reg_form = ProfileForm(request.POST)
        if form.is_valid() and p_reg_form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            p_reg_form = ProfileForm(request.POST, instance=user.profile)
            p_reg_form.full_clean()
            p_reg_form.save()
        return redirect('login')
    else:
        form = RegisterUserForm()
        p_reg_form = ProfileForm()
    context = {'form': form, 'p_reg_form': p_reg_form}
    return render(request, 'dvlink/signin.html', context)


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                # Сохранение токена аутентификации в Local Storage
                # Получаем профиль пользователя
                profile = Profile.objects.get(user=user)

                # Получаем или создаем токен авторизации пользователя
                token, created = Token.objects.get_or_create(user=user)

                # Получаем значение ключа токена
                token_key = token.key
                request.session['token'] = token_key
                return redirect('account')
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'dvlink/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')


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


def delete_application(pk):
    application = get_object_or_404(Applications, pk=pk)
    application.delete()
    return JsonResponse({'message': 'Запись успешно удалена'})

