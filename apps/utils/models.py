from django.db import models
from django.contrib.auth import get_user_model

from apps.blogs.models import Blog

User = get_user_model()


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    auth = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE, related_name='auth')
    content = models.TextField(verbose_name='评论内容')
    date_time = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')

    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,related_name='son_comment')
    root = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,related_name='root_comment')
    reply_auth = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,related_name='reply_auth')


    def __str__(self):
        return '%s:%s'%(self.auth, self.content)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论'
