from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404, ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from .forms import *
from .models import *
from django.contrib.auth.models import *

from .pagination import ApplicationsPagination
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

    posts = Applications.objects.filter(user=request.user).order_by('user_order_id')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'dvlink/account.html', {'page_obj': page_obj, 'form': form, 'title': 'Аккаунт'})


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
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if password1 == password2:
                user = form.save()
                user.refresh_from_db()
                p_reg_form = ProfileForm(request.POST, instance=user.profile)
                p_reg_form.full_clean()
                p_reg_form.save()
                return redirect('login')
            else:
                messages.error(request, 'Пароли не совпадают')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
            for field, errors in p_reg_form.errors.items():
                for error in errors:
                    messages.error(request, error)
    else:
        form = RegisterUserForm()
        p_reg_form = ProfileForm()

    context = {'form': form, 'p_reg_form': p_reg_form}
    return render(request, 'dvlink/signin.html', context)


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
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
                messages.error(request, 'Неправильное имя пользователя или пароль')
        else:
            messages.error(request, 'Неправильное имя пользователя или пароль')
    else:
        form = UserLoginForm()

    context = {'form': form}
    return render(request, 'dvlink/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')


class ApplicationsListView(ListAPIView):
    queryset = Applications.objects.all()
    serializer_class = ApplicationsSerializer
    pagination_class = ApplicationsPagination

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


def delete_application(request, pk):
    application = get_object_or_404(Applications, pk=pk)
    user_id = application.user_id
    application.delete()

    update_application_order_numbers(user_id)

    return JsonResponse({'message': 'Запись успешно удалена'})

def update_application_order_numbers(user_id):
    user_applications = Applications.objects.filter(user_id=user_id).order_by('user_order_id')
    for index, application in enumerate(user_applications, start=1):
        application.user_order_id = index
        application.save()

