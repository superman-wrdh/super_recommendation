from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes


# Create your views here.


@api_view(http_method_names=['POST', ])
@permission_classes((permissions.AllowAny,))
def first_api(request):
    params = request.data
    resp = {'success': True}
    try:

        resp.update({'records': params})
    except Exception as e:
        resp.update({'success': False, 'msg': str(e)})
    return Response(resp, status=status.HTTP_200_OK)
