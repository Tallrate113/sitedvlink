from django.contrib.auth.models import User
from django.db import models
from django.db.models import Max
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Applications(models.Model):
    id = models.AutoField(primary_key=True)
    field_organisation_name = models.CharField(max_length=255, verbose_name = 'Организация')
    field_text_appeal = models.CharField(max_length=255, verbose_name = 'Обращение')
    stat = models.ForeignKey('Status', on_delete=models.PROTECT, verbose_name = 'Статус', default=1)
    emp = models.ForeignKey('Employee', on_delete=models.PROTECT, verbose_name = 'Сотрудник', null=True)
    field_number_phone = models.CharField(max_length=18, verbose_name='Телефон', null=True)
    field_email = models.EmailField(max_length=255, verbose_name='E-mail', null=True)
    field_fio = models.CharField(max_length=255, verbose_name='ФИО', null=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, null=True)
    user_order_id = models.PositiveIntegerField(verbose_name='Порядковый номер заявки', default=1)

    def __str__(self):
        return self.field_organisation_name

    class Meta:
        verbose_name = 'Заявки'
        verbose_name_plural = 'Заявки'
        ordering = ['-time_create']

    def save(self, *args, **kwargs):
        if not self.pk:  # если объект только что создан
            max_user_order_id = Applications.objects.filter(user=self.user).aggregate(Max('user_order_id'))[
                'user_order_id__max']
            self.user_order_id = max_user_order_id + 1 if max_user_order_id else 1
        super().save(*args, **kwargs)


class Status(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name = 'Статус')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус заявки'
        verbose_name_plural = 'Статус заявки'
        ordering = ['id', ]


class Employee(models.Model):
    name = models.CharField(max_length=30, verbose_name = 'Сотрудник')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудник'
        ordering = ['id', ]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisation_name = models.CharField(max_length=255, verbose_name = 'Организация', null=True)
    number_phone = models.CharField(max_length=18, verbose_name='Телефон', null=True)
    auth_token = models.OneToOneField(Token, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def update_profile_signal(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
            Token.objects.create(user=instance)
        instance.profile.save()
