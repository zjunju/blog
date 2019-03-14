import uuid
import os

from django.db import models
from django.core.validators import RegexValidator, FileExtensionValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, AbstractUser


def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:8], ext)
    sub_folder = "img"
    return os.path.join(instance.user.id, sub_folder, filename)


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, telephone, username, password, **extra_fields):
        if not telephone:
            return ValueError('手机号码不能为空')
        if not username:
            return ValueError('用户名不能为空')
        if not password:
            return ValueError('密码不能为空')

        user = self.model(telephone=telephone, username=username, **extra_fields)
        user.set_password(password=password)
        user.save()
        return user


    def create_user(self, telephone, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(telephone, username, password, **extra_fields)


    def create_superuser(self, telephone, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self._create_user(telephone, username, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    telephone = models.CharField(max_length=11, validators=[RegexValidator(regex=r"^1[345678][0-9]{9}",message="请输入有效的手机号码")], unique=True,verbose_name="手机号码")
    username = models.CharField(max_length=50, verbose_name='用户名', unique=True)
    img = models.ImageField(upload_to= user_directory_path, verbose_name="用户头像", validators=[FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg'],message='只允许上传png、jpeg、jpg格式的头像')])
    email = models.EmailField(blank=True, null=True, verbose_name='邮箱')
    is_staff = models.BooleanField(default=False, verbose_name='是否职员')
    is_active = models.BooleanField(default=False, verbose_name='是否激活')
    date_join = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'telephone'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = '用户表'
        verbose_name_plural = '用户表'
