from django.db import models

class Applications(models.Model):
    organization = models.CharField(max_length=255, verbose_name = 'Организация')
    appeal = models.TextField(blank=True, verbose_name = 'Обращение')
    stat = models.ForeignKey('Status', on_delete=models.PROTECT, verbose_name = 'Статус')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name = 'Время создания')
    emp = models.ForeignKey('Employee', on_delete=models.PROTECT, verbose_name = 'Сотрудник')
    def __str__(self):
        return self.organization

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

