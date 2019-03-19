from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model

from apps.utils.base_form import FormsMixin


User = get_user_model()


class AuthSigninForm(forms.Form, FormsMixin):
    username = forms.CharField(error_messages={'required': '请输入手机号码或者用户名'})
    password = forms.CharField(error_messages={'required': '请输入密码'})
    remember = forms.BooleanField(required=False)


class AuthSignupForm(forms.Form, FormsMixin):
    telephone = forms.CharField(validators=[RegexValidator(regex=r'^1[3456789]\d{9}', message='请输入正确的手机号码!')],error_messages={'required': '请输入手机号码'})
    username = forms.CharField(error_messages={'required': '请输入手机号码或者用户名'})
    password = forms.CharField(min_length=8, error_messages={'required': '请输入密码', 'min_length': '请输入大于8位数的密码！'})
    password_reply = forms.CharField(error_messages={'required': '请再次输入密码'})


    def clean(self):
        cleaned_data = super(AuthSignupForm, self).clean()
        telephone = cleaned_data.get('telephone')
        password = cleaned_data.get('password')
        password_reply = cleaned_data.get('password_reply')

        user = User.objects.filter(telephone=telephone).first()
        if user:
            raise forms.ValidationError(code="exists", message='该手机号码已经被注册！')

        if password != password_reply:
            raise forms.ValidationError(code="different", message='两次密码不一致！')

