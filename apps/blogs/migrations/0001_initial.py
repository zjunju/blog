# Generated by Django 2.1.7 on 2019-03-14 02:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='博客标题')),
                ('pub_time', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='%Y-%m-%d', verbose_name='博客缩略图')),
                ('love', models.PositiveIntegerField(default=0, verbose_name='点赞数')),
                ('read_times', models.PositiveIntegerField(default=0, verbose_name='阅读数')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
        ),
        migrations.CreateModel(
            name='ReadDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rd_times', models.PositiveIntegerField(default=0, verbose_name='阅读数')),
                ('date_join', models.DateField(auto_now_add=True, verbose_name='阅读日期')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=50, verbose_name='标签')),
                ('date_join', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
    ]