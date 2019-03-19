from apps.utils.restfulAPI import restful


def authenticate_user(get_response):
    ''' 网站初始化时执行的代码片段 '''

    def middleware(request):
        ''' 浏览器发送请求到达视图函数之前，也就是执行视图函数之前执行的代码片段 '''
        # 判断用户是否已经登录
        user = request.user
        if not user.is_authenticated:
            return restful.un_signup(message='用户未登录')

        response = get_response(request)
        # 执行了视图函数之后返回response，执行的代码片段
        return response

    return middleware()