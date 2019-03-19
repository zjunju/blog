# Generated by Django 2.1.7 on 2019-03-17 14:26

import apps.users.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190314_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=apps.users.models.user_directory_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg'], message='只允许上传png、jpeg、jpg格式的头像')], verbose_name='用户头像'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=20, unique=True, verbose_name='用户名'),
        ),
    ]
