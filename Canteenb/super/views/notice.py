# 2023-12-04
# 管理员端：通知管理，增删改查
import json
import time

from django.core.paginator import Paginator
from django.db.models import Q
from django.forms import model_to_dict
from django.http import JsonResponse
from comment.models import Notifications
from customer.models import Customer
from lib.handler import request_handler


def add(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        noti_title = data.get('noti_title')
        noti_content = data.get('noti_content')
        username = data.get('username')  # 改为接收username
        noti_sendtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

        # 通过username查找对应的Customer对象
        try:
            customer = Customer.objects.get(username=username)
        except Customer.DoesNotExist:
            return JsonResponse({'code': 2, 'info': '用户不存在'})

        if noti_title and noti_content and customer:
            new_noti = Notifications.objects.create(
                noti_title=noti_title,
                noti_content=noti_content,
                noti_sendtime=noti_sendtime,
                cus_id_id=customer.id
            )
            return JsonResponse({'code': 0, 'info': '通知添加成功，id为' + str(new_noti.id)})
        else:
            return JsonResponse({'code': 1, 'info': '提交参数缺失'})
    else:
        return JsonResponse({'code': 1, 'info': '禁止使用该方法提交数据'})


def delete(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        noti_id = data.get('noti_id')
        if noti_id:
            try:
                noti = Notifications.objects.get(id=noti_id)
                noti.delete()
                return JsonResponse({'code': 0, 'info': '通知删除成功'})
            except Notifications.DoesNotExist:
                return JsonResponse({'code': 1, 'info': '删除失败，通知不存在'})
        else:
            return JsonResponse({'code': 1, 'info': '删除失败，未找到通知'})
    else:
        return JsonResponse({'code': 1, 'info': '禁止使用该方法提交数据'})


def update(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        noti_id = data.get('noti_id')
        noti_title = data.get('noti_title')
        noti_content = data.get('noti_content')
        if noti_id:
            try:
                noti = Notifications.objects.get(id=noti_id)
                if noti_title:
                    noti.noti_title = noti_title
                if noti_content:
                    noti.noti_content = noti_content
                noti.save()
                return JsonResponse({'code': 0, 'info': '通知修改成功'})
            except:
                return JsonResponse({'code': 1, 'info': '修改失败'})
        else:
            return JsonResponse({'code': 1, 'info': '修改失败，未找到通知'})
    else:
        return JsonResponse({'code': 1, 'info': '禁止使用该方法提交数据'})


def query(request):
    if request.method == 'GET':
        keys = request.GET.get('keys', None)
        pagenum = request.GET.get('pagenum')
        pagesize = request.GET.get('pagesize')
        if pagenum is not None and pagesize is not None:
            pagenum = int(pagenum)
            pagesize = int(pagesize)
            noti_list = Notifications.objects.all().order_by('-id')
            if keys:
                conditions = [Q(noti_title__contains=con) for con in keys.split(' ') if con]
                querys = Q()
                for condi in conditions:
                    querys &= condi
                noti_list = noti_list.filter(querys)
            paginator = Paginator(noti_list, pagesize)
            page = paginator.get_page(pagenum)

            res = []
            for obj in page.object_list:
                cus_id = obj.cus_id_id  # 获取cus_id_id字段
                customer = Customer.objects.get(pk=cus_id) if cus_id else None
                username = customer.username if customer else None
                noti_dict = model_to_dict(obj)
                noti_dict['noti_cus'] = username
                res.append(noti_dict)

            return JsonResponse({'code': 0, 'info': '查询成功', 'list': res, 'total': paginator.count})
        else:
            return JsonResponse({'code': 1, 'info': '提交数据缺失'})
    else:
        return JsonResponse({'code': 1, 'info': '请求方式错误'})

options = {
    'add': add,
    'delete': delete,
    'update': update,
    'query': query
}

def handler(request):
    return request_handler(request, options)
