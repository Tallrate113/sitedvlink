# Generated by Django 4.2.1 on 2023-05-30 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvlink', '0008_applications_field_email_applications_field_fio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='applications',
            name='time_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Время изменения'),
        ),
    ]