from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.authtoken.models import Token
import os

# Create your views here.
from super_recommendation.settings import BASE_DIR
from uuid import uuid4


@api_view(http_method_names=['POST', ])
@permission_classes((permissions.AllowAny,))
def first_api(request):
    params = request.data
    file_obj = request.FILES.get("img")
    f = open(os.path.join(BASE_DIR, "templates", "upload", file_obj.name), 'wb')
    for i in file_obj.chunks():
        f.write(i)
    f.close()
    resp = {'success': True}
    try:
        resp.update({'records': file_obj.name})
    except Exception as e:
        resp.update({'success': False, 'msg': str(e)})
    return Response(resp, status=status.HTTP_200_OK)


def _user_exit_check(user_name):
    user = User.objects.filter(username=user_name).first()
    if user:
        return True
    else:
        return False


def _validate_user_password(user_name, password):
    user = User.objects.filter(username=user_name).first()
    result = {}
    if user:
        r = user.check_password(password)
        if r:
            result.update({"status": True, "msg": "密码正确", "user_id": user.username, "auth": user.last_name})
        else:
            result.update({"status": False, "msg": "密码错误"})
    else:
        result.update({"status": False, "msg": "用户不存在"})
    return result


def validate_email_reg_code():
    """
    TODO
    注册 找回密码发送验邮件证码
    """
    return ""


def _create_user_check(user_name):
    is_exit = _user_exit_check(user_name)
    result = {}
    if is_exit:
        result.update({"status": False, "msg": "用户名已经注册"})
    else:
        result.update({"status": True, "msg": "可以注册"})
    return result


@api_view(http_method_names=['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def register(request):
    """
    注册
    """
    param = request.data
    reg_code = param.get("reg_code")
    mobile = param.get("mobile")
    email = param.get("email")
    user_name = param.get("user_name")
    password = param.get("password")
    resp = {'success': True}
    try:
        r = validate_email_reg_code(mobile=mobile, message_code=reg_code)
        if r['status']:
            cr = _create_user_check(user_name)
            if cr['status']:
                user = User(username=str(mobile), email=email, last_name="0")
                user.set_password(password)
                user.save()
                resp.update({'success': True, 'records': {"user_id": mobile}})
            else:
                resp.update({'success': True, 'records': cr['msg']})
        else:
            resp.update({'success': False, 'msg': r['msg']})
    except Exception as e:
        resp.update({'success': False, 'msg': str(e)})
    finally:
        return Response(resp, status=status.HTTP_200_OK)


@api_view(http_method_names=['POST', ])
@permission_classes((permissions.AllowAny,))
def user_login(request):
    params = request.data
    username = params.get("user_name", None)
    user_pass = params.get("user_pass", None)
    resp = {'success': True}
    try:
        exit = _user_exit_check(username)
        if not exit:
            resp.update({'success': False, 'msg': "用户不存在"})
        else:
            validate = _validate_user_password(user_name=username, password=user_pass)
            if validate['status']:
                resp = {'success': True, 'msg': validate['status']}
                user = User.objects.filter(username=username).first()
                Token.objects.filter(user=user).delete()
                token = Token.objects.create(user=user)
                token_value = token.key
                resp.update({'success': True, 'token': str(token_value), 'msg': validate['status']})
            else:
                resp.update({'success': False, 'msg': validate['status']})
    except Exception as e:
        resp.update({'success': False, 'msg': str(e)})
    return Response(resp, status=status.HTTP_200_OK)


@api_view(http_method_names=['POST', ])
@permission_classes((permissions.AllowAny,))
def search(request):
    params = request.data
    resp = {'success': True}
    try:
        records = []
        resp.update({'records': records})
    except Exception as e:
        resp.update({'success': False, 'msg': str(e)})
    return Response(resp, status=status.HTTP_200_OK)


@api_view(http_method_names=['POST', ])
@permission_classes((permissions.AllowAny,))
def add(request):
    params = request.data
    resp = {'success': True}
    try:
        records = []
        resp.update({'records': records})
    except Exception as e:
        resp.update({'success': False, 'msg': str(e)})
    return Response(resp, status=status.HTTP_200_OK)


@api_view(http_method_names=['POST', ])
@permission_classes((permissions.AllowAny,))
def update(request):
    params = request.data
    resp = {'success': True}
    try:
        records = []
        resp.update({'records': records})
    except Exception as e:
        resp.update({'success': False, 'msg': str(e)})
    return Response(resp, status=status.HTTP_200_OK)


@api_view(http_method_names=['POST', ])
@permission_classes((permissions.IsAuthenticated,))
def delete(request):
    params = request.data
    resp = {'success': True}
    try:
        records = []
        resp.update({'records': records})
    except Exception as e:
        resp.update({'success': False, 'msg': str(e)})
    return Response(resp, status=status.HTTP_200_OK)
