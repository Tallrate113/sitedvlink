# Generated by Django 4.2.1 on 2023-06-05 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvlink', '0011_applications_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='applications',
            name='user',
        ),
    ]
