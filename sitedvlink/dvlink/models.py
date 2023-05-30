from django.db import models

class Applications(models.Model):
    field_organisation_name = models.CharField(max_length=255, verbose_name = 'Организация')
    field_text_appeal = models.CharField(max_length=255, verbose_name = 'Обращение')
    stat = models.ForeignKey('Status', on_delete=models.PROTECT, verbose_name = 'Статус', null=True)
    emp = models.ForeignKey('Employee', on_delete=models.PROTECT, verbose_name = 'Сотрудник', null=True)
    field_number_phone = models.CharField(max_length=255, verbose_name='Телефон', null=True)
    field_email = models.EmailField(max_length=255, verbose_name='E-mail', null=True)
    field_fio = models.CharField(max_length=255, verbose_name='ФИО', null=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

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


