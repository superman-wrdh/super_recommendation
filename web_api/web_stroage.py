# -*- encoding: utf-8 -*-
import os

from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

# Create your views here.
from super_recommendation.settings import BASE_DIR


@api_view(http_method_names=['POST', ])
@permission_classes((permissions.AllowAny,))
def upload_file(request):
    """
    多文件上传文件
    """
    params = request.data
    # request.FILES.get('file') 单文件
    files = params.getlist('file', None)  # 多文件
    names = []
    resp = {'success': True}
    try:
        for file_obj in files:
            mine_type = file_obj.content_type
            file_name = file_obj.name
            file_size = file_obj.size
            f = open(os.path.join(BASE_DIR, "templates", "upload", file_obj.name), 'wb')
            for i in file_obj.chunks():
                f.write(i)
            f.close()
            print('文件名', file_name, '文件类型', mine_type, '文件大小', file_size, 'B')
            names.append(file_name)
        resp['name'] = names
    except Exception as e:
        resp.update({'success': False, 'msg': str(e)})
    return Response(resp, status=status.HTTP_200_OK)


def get_file():
    """
    根据文件id返回文件流  仅能查看不需要权限的文件
    """
    pass


def load_file():
    """
    获取文件 管理员调用接口 查看全部文件
    """
    pass
