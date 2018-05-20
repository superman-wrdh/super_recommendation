from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

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
