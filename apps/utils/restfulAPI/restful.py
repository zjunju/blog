from django.http import JsonResponse


class HttpCode(object):
    ok = '200'
    donothing = '202'
    paramserror = '400'
    unsignin = '401'
    internalerror = '500'


def result(code=HttpCode.ok, message='', data=None, **kwargs):
    json_data = {'code': code, 'message': message, 'data': data}
    if kwargs and isinstance(kwargs, dict):
        json_data.update(kwargs)
    return JsonResponse(json_data, json_dumps_params={'ensure_ascii': False})

def ok():
    return result()

def un_signup(message='', data=None, **kwargs):
    return result(code=HttpCode.unsignin, message=message, data=data, **kwargs)

def params_error(message='', data=None, **kwargs):
    return result(code=HttpCode.paramserror, message=message, data=data, **kwargs)

def internal_error(message='', data=None, **kwargs):
    return result(code=HttpCode.internalerror, message=message, data=data, **kwargs)

def do_nothing(message='', data=None, **kwargs):
    return result(code=HttpCode.donothing, message=message, data=data, *kwargs)
