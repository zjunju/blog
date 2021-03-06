# Generated by Django 2.1.7 on 2019-03-13 15:26

import apps.users.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('telephone', models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(message='请输入有效的手机号码', regex='^1[345678][0-9]{9}')], verbose_name='手机号码')),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='用户名')),
                ('img', models.ImageField(upload_to=apps.users.models.user_directory_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg'], message='只允许上传png、jpeg、jpg格式的头像')], verbose_name='用户头像')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='邮箱')),
                ('is_staff', models.BooleanField(default=False, verbose_name='是否职员')),
                ('is_active', models.BooleanField(default=False, verbose_name='是否激活')),
                ('date_join', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户表',
                'verbose_name_plural': '用户表',
            },
            managers=[
                ('objects', apps.users.models.UserManager()),
            ],
        ),
    ]
