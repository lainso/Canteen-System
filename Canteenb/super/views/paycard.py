# 2023-12-13
# 管理员端：支付卡管理-删改查
import json
import random
import string
import time

from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.forms import model_to_dict
from django.http import JsonResponse

from customer.models import Customer, Paycard
from lib.handler import request_handler


def delete(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        card_id = data.get('card_id')
        if card_id:
            try:
                paycard = Paycard.objects.get(id=card_id)
                paycard.delete()
                return JsonResponse({'code': 0, 'info': '支付卡删除成功'})
            except Paycard.DoesNotExist:
                return JsonResponse({'code': 1, 'info': '删除失败，支付卡不存在'})
        else:
            return JsonResponse({'code': 1, 'info': '删除失败，缺少接口必要参数'})
    else:
        return JsonResponse({'code': 1, 'info': '禁止使用该方法提交数据'})


def update(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        card_id = data.get('card_id')
        card_balance = data.get('card_balance')
        card_condition = data.get('card_condition')
        if card_id:
            try:
                card = Paycard.objects.get(id=card_id)
                if card_balance:
                    card.card_balance = card_balance
                if card_condition:
                    card.card_condition = card_condition
                card.save()
                return JsonResponse({'code': 0, 'info': '支付卡信息修改成功'})
            except Paycard.DoesNotExist:
                return JsonResponse({'code': 1, 'info': '修改失败，支付卡不存在'})
        else:
            return JsonResponse({'code': 1, 'info': '修改失败，缺少接口必要参数'})
    else:
        return JsonResponse({'code': 1, 'info': '禁止使用该方法提交数据'})


def query(request):
    if request.method == 'GET':
        username = request.GET.get('username', None)
        pagenum = request.GET.get('pagenum')
        pagesize = request.GET.get('pagesize')

        try:
            pagenum = int(pagenum)
            pagesize = int(pagesize)
        except (TypeError, ValueError):
            return JsonResponse({'code': 1, 'info': '分页参数必须是整数'})

        if pagenum and pagesize:
            card_list = Paycard.objects.all().order_by('-id')

            if username:
                customers = Customer.objects.filter(username__icontains=username)
                customer_ids = customers.values_list('id', flat=True)
                card_list = card_list.filter(cus_id__in=customer_ids)

            paginator = Paginator(card_list, pagesize)

            try:
                page = paginator.page(pagenum)
            except EmptyPage:
                return JsonResponse({'code': 1, 'info': '页码超出范围'})

            card_ids = list(page.object_list.values_list('id', flat=True))
            cards_with_usernames = []
            for card_id in card_ids:
                card = Paycard.objects.get(id=card_id)
                card_data = model_to_dict(card)
                card_data['username'] = card.cus_id.username
                cards_with_usernames.append(card_data)

            return JsonResponse({'code': 0, 'info': '查询成功', 'list': cards_with_usernames, 'total': paginator.count})
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
