from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Applications(models.Model):
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

    def __str__(self):
        return self.field_organisation_name

    class Meta:
        verbose_name = 'Заявки'
        verbose_name_plural = 'Заявки'
        ordering = ['-time_create']


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

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def update_profile_signal(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()
