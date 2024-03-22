# 2023-12-09
# 管理员端：促销管理-增删改查
import json

from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse

from comment.models import Promotions
from lib.handler import request_handler


def add(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('promo_name')
        code = data.get('promo_code')
        multi = data.get('promo_muti')
        start = data.get('promo_start')
        end = data.get('promo_end')
        if name and code and multi and start and end:
            new_promo = Promotions.objects.create(promo_name=name, promo_code=code, promo_multiple=multi,
                                                  promo_start=start, promo_end=end)
            return JsonResponse({'code': 0, 'info': '促销活动添加成功，id为' + str(new_promo.id)})
        else:
            return JsonResponse({'code': 1, 'info': '提交参数缺失'})
    else:
        return JsonResponse({'code': 1, 'info': '禁止使用该方法提交数据'})


def delete(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        promo_id = data.get('promo_id')
        if promo_id:
            try:
                Promotions.objects.get(id=promo_id).delete()
                return JsonResponse({'code': 0, 'info': '促销活动删除成功'})
            except Promotions.DoesNotExist:
                return JsonResponse({'code': 1, 'info': '促销活动不存在'})
        else:
            return JsonResponse({'code': 1, 'info': '提交参数缺失'})
    else:
        return JsonResponse({'code': 1, 'info': '禁止使用该方法提交数据'})


def update(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        promo_id = data.get('promo_id')
        promo_data = data.get('promo_data')
        if promo_id and promo_data:
            try:
                promo = Promotions.objects.get(id=promo_id)
            except Promotions.DoesNotExist:
                return JsonResponse({'code': 1, 'info': '促销活动不存在'})
            if 'promo_name' in promo_data:
                promo.promo_name = promo_data['promo_name']
            if 'promo_code' in promo_data:
                promo.promo_code = promo_data['promo_code']
            if 'promo_multi' in promo_data:
                promo.promo_multiple = promo_data['promo_multi']
            if 'promo_start' in promo_data:
                promo.promo_start = promo_data['promo_start']
            if 'promo_end' in promo_data:
                promo.promo_end = promo_data['promo_end']
            promo.save()
            return JsonResponse({'code': 0, 'info': '促销活动修改成功'})
        else:
            return JsonResponse({'code': 1, 'info': '提交参数缺失'})
    else:
        return JsonResponse({'code': 1, 'info': '禁止使用该方法提交数据'})


def query(request):
    if request.method == 'GET':
        keys = request.GET.get('keys')
        pagesize = request.GET.get('pagesize')
        pagenum = request.GET.get('pagenum')

        if pagesize and pagenum:
            promo_list = Promotions.objects.all().order_by('-id')
            if keys:
                conditions = [Q(promo_name__contains=con) for con in keys.split(' ') if con]
                querys = Q()
                for condi in conditions:
                    querys &= condi
                promo_list = promo_list.filter(querys)
            paginator = Paginator(promo_list, pagesize)
            page = paginator.get_page(pagenum)
            res = list(page.object_list.values())
            return JsonResponse({'code': 0, 'info': '查询成功', 'list': res, 'total': paginator.count})
        else:
            return JsonResponse({'code': 1, 'info': '查询失败，有缺失的参数未提交'})
    else:
        return JsonResponse({'code': 1, 'info': '查询失败，禁止使用该方法提交'})


options = {
    'add': add,
    'delete': delete,
    'update': update,
    'query': query
}


def handler(request):
    return request_handler(request, options)
