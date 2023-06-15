# Generated by Django 4.2.1 on 2023-06-15 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authtoken', '0003_tokenproxy'),
        ('dvlink', '0018_alter_profile_organisation_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='auth_token',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authtoken.token'),
        ),
    ]
