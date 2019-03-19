from functools import wraps


def authenticate_user(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return restful.un_signup(message='请先登录')
        return func(request, *args, **kwargs)

    return wrapper
