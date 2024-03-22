# 2023-12-12
# 管理员端：交易记录管理-增删改查
import json
import random
import string
import time

from django.core.paginator import Paginator
from django.db.models import Q
from django.forms import model_to_dict
from django.http import JsonResponse

from comment.models import Payment
from lib.handler import request_handler
from shop.models import Order


def delete(request):
    if request.method == 'POST':
        pay_id = request.params['pay_id']
        if pay_id:
            try:
                payment = Payment.objects.get(id=pay_id)
                payment.delete()
                return JsonResponse({'code': 0, 'info': '支付记录删除成功'})
            except Payment.DoesNotExist:
                return JsonResponse({'code': 1, 'info': '删除失败，支付记录不存在'})
        else:
            return JsonResponse({'code': 1, 'info': '删除失败，未找到支付记录'})
    else:
        return JsonResponse({'code': 1, 'info': '禁止使用该方法提交数据'})


def update(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        pay_id = data.get('pay_id')
        pay_money = data.get('pay_money')
        pay_way = data.get('pay_way')
        if pay_id:
            try:
                pay = Payment.objects.get(id=pay_id)
                if pay_money:
                    pay.pay_money = pay_money
                if pay_way:
                    pay.pay_way = pay_way
                pay.save()
                return JsonResponse({'code': 0, 'info': '支付记录修改成功'})
            except Payment.DoesNotExist:
                return JsonResponse({'code': 1, 'info': '修改失败，支付记录不存在'})
        else:
            return JsonResponse({'code': 1, 'info': '修改失败，未找到支付记录'})
    else:
        return JsonResponse({'code': 1, 'info': '禁止使用该方法提交数据'})


def query(request):
    if request.method == 'GET':
        keys = request.GET.get('keys', None)
        pagenum = request.GET.get('pagenum', None)
        pagesize = request.GET.get('pagesize', None)

        if pagenum and pagesize:
            pagenum, pagesize = int(pagenum), int(pagesize)
            # 假设Payment和Order通过order字段相关联
            pay_list = Payment.objects.select_related('ord_id').all().order_by('-id')

            if keys:
                conditions = [Q(pay_time__contains=con) for con in keys.split(' ') if con]
                querys = Q()
                for condi in conditions:
                    querys &= condi
                pay_list = pay_list.filter(querys)

            paginator = Paginator(pay_list, pagesize)
            page = paginator.get_page(pagenum)

            # 创建一个包含Payment信息以及相关联Order的ord_number的列表
            res = [model_to_dict(payment) for payment in page.object_list]
            for item, payment in zip(res, page.object_list):
                item.update({'order_number': payment.ord_id.ord_number})

            return JsonResponse({
                'code': 0,
                'info': '查询成功',
                'list': res,
                'total': paginator.count
            })
        else:
            return JsonResponse({'code': 1, 'info': '提交数据缺失'})
    else:
        return JsonResponse({'code': 1, 'info': '请求方式错误'})


options = {
    'delete': delete,
    'update': update,
    'query': query
}


def handler(request):
    return request_handler(request, options)
