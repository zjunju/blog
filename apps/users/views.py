from django.shortcuts import render, reverse, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.views.decorators.http import require_GET, require_POST

from .forms import AuthSigninForm, AuthSignupForm

from apps.utils.restfulAPI import restful

User = get_user_model()


@require_POST
def signin(request):
    form = AuthSigninForm(request.POST)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        username = cleaned_data.get('username', None)
        password = cleaned_data.get('password', None)
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            remember = cleaned_data.get('remember', False)
            if remember:
                # 如果设置为None，则session使用settings.py文件中默认的session保存时间，为两周
                request.session.set_expiry(None)
            else:
                # 设置为0， 则表示浏览器关闭时，session也消失。
                request.session.set_expiry(0)
            return restful.ok()
        else:
            return restful.params_error(message='密码不匹配')
    else:
        errors = form.get_json_error()
        return restful.params_error(message=errors)


@require_POST
def signup(request):
    form = AuthSignupForm(request.POST)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        username = cleaned_data.get('username')
        telephone = cleaned_data.get('telephone')
        password = cleaned_data.get('password')
        try:
            user = User.objects.create_user(username=username, password=password, telephone=telephone)
            login(request, user)
            return restful.ok()
        except Exception as e:
            print(e)
            return restful.internal_error(message="未知错误！")

    else:
        errors = form.get_json_error()
        return restful.params_error(message=errors)


@require_GET
def logout_view(request):
    logout(request)

    return redirect(request.META.get('HTTP_REFERER', '/'))

