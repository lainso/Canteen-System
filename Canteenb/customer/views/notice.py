# 2023-12-04
# 客户端：通知管理——获取通知
import json

from django.core import serializers
from django.core.paginator import Paginator
from django.http import JsonResponse

from comment.models import Notifications
from customer.models import Customer


def query(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        pagesize = request.GET.get('pagesize')
        pagenum = request.GET.get('pagenum')

        if username and pagesize and pagenum:
            customer = Customer.objects.get(username=username)
            noti_list = Notifications.objects.filter(cus_id_id=customer.id).order_by('id')
            paginator = Paginator(noti_list, pagesize)
            page = paginator.get_page(pagenum)

            noti_list_json = serializers.serialize('json', page)
            data = json.loads(noti_list_json)
            return JsonResponse({'code': 0, 'info': '查询成功', 'list': data, 'total': paginator.count})
        else:
            return JsonResponse({'code': 1, 'info': '提交数据缺失'})
    else:
        return JsonResponse({'code': 1, 'info': '请求方式错误'})
