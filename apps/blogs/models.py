import os

from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

from ckeditor_uploader.fields import RichTextUploadingField

User = get_user_model()

class ReadDetail(models.Model):
    rd_times = models.PositiveIntegerField(default=0, verbose_name='阅读数')
    date_join = models.DateField(auto_now_add=True, verbose_name='阅读日期')

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()

    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return '<%s:%s:%s>'%(self.content_object, self.rd_times, self.date_join)


class Tags(models.Model):
    tag_name = models.CharField(max_length=50, verbose_name='标签')
    date_join = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tag_name


# 自定义博客缩略图上传目录
def blog_thumbnail_event(instance, file_name):
    title = instance.title
    if title is None:
        raise ValueError('请输入博客标题')
    if file_name is None:
        raise ValueError('请上传图片')

    upload_path = os.path.join('blog_thumbnail', title, file_name)

    return upload_path


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name='博客标题')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    content = RichTextUploadingField(verbose_name='内容')
    pub_time = models.DateTimeField(auto_now_add=True,verbose_name='发布时间')
    thumbnail = models.ImageField(upload_to=blog_thumbnail_event, verbose_name='博客缩略图', blank=True,null=True)
    love = models.PositiveIntegerField(default=0, verbose_name='点赞数')
    read_times = models.PositiveIntegerField(default=0, verbose_name='阅读数')
    tags = models.ManyToManyField(Tags, related_name='blogs', verbose_name='标签')
    rd_detail = GenericRelation(ReadDetail)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '博客'
        verbose_name_plural = '博客'
        ordering = ['-pub_time']
