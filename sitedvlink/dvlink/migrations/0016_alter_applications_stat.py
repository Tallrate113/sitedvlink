# Generated by Django 4.2.1 on 2023-06-05 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dvlink', '0015_alter_applications_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='stat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='dvlink.status', verbose_name='Статус'),
        ),
    ]
