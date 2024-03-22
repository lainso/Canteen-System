# 2023-11-28
# 商户端：订单管理，增改查自己的订单
import json
import random
import string
import time

from django.core.paginator import Paginator
from django.db.models import Q
from django.forms import model_to_dict
from django.http import JsonResponse

from customer.models import Customer
from lib.handler import request_handler
from shop.models import Order, OrderList, Shop


#   商户添加订单
def add(request):
    if request.method == 'POST':
        # 生成17位的订单号
        ord_number = str(int(time.time())) + ''.join(random.sample(string.ascii_letters + string.digits, 7))
        ord_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        data = json.loads(request.body)
        username = data.get('username')
        user = data.get('user')
        ord_condition = data.get('ord_condition')
        order_list = data.get('ord_list')
        ord_money = data.get('money')
        if username and user and ord_money and order_list:
            try:
                customer = Customer.objects.get(username=username)
                user = Customer.objects.get(username=user)
                shop = Shop.objects.get(shop_cus=user.id)
                new_order = Order.objects.create(ord_number=ord_number, ord_time=ord_time, cus_id=customer,
                                                 ord_shop=shop, ord_condition=ord_condition, ord_money=ord_money)
                batch = [OrderList(ord_number_id=ord_number, dish_id=record['dish_id'], ordlist_num=record['count'])
                         for record in json.loads(order_list)]
                status = OrderList.objects.bulk_create(batch)
                if status:
                    return JsonResponse({'code': 0, 'info': '订单添加成功', 'id': str(new_order.id)})
                else:
                    return JsonResponse({'code': 1, 'info': '订单添加失败'})
            except Customer.DoesNotExist:
                return JsonResponse({'code': 1, 'info': '添加订单失败，请检查用户账号是否输入正确！'})
            except Exception as e:
                return JsonResponse({'code': 1, 'info': '添加订单失败：' + str(e)})
        else:
            return JsonResponse({'code': 1, 'info': '提交数据缺失'})
    else:
        return JsonResponse({'code': 1, 'info': '请求方式错误'})


def update(request):
    if request.method == 'POST':
        ord_number = request.params['ord_number']
        ord_condition = request.params['ord_condition']
        if ord_number:
            try:
                order = Order.objects.get(ord_number=ord_number)
                order.ord_condition = ord_condition
                order.save()
                return JsonResponse({'code': 0, 'info': '订单修改成功'})
            except Exception as e:
                return JsonResponse({'code': 1, 'info': '订单修改失败：' + str(e)})
        else:
            return JsonResponse({'code': 1, 'info': '订单号缺失'})
    else:
        return JsonResponse({'code': 1, 'info': '请求方式错误'})


#  商户查询自己的订单
def query(request):
    if request.method == 'GET':
        keys = request.GET.get('keys', None)
        pagenum = request.GET.get('pagenum', None)
        pagesize = request.GET.get('pagesize', None)
        username = request.GET.get('username', None)

        if pagesize and pagenum and username:
            user = Customer.objects.get(username=username)
            shop = Shop.objects.get(shop_cus=user.id)
            order_list = Order.objects.select_related('cus_id', 'ord_shop').all().order_by('-id').filter(
                ord_shop=shop.id)

            if keys:
                conditions = [Q(ord_time__contains=con) for con in keys.split(' ') if con]
                querys = Q()
                for condi in conditions:
                    querys &= condi
                order_list = order_list.filter(querys)

            paginator = Paginator(order_list, pagesize)
            page = paginator.get_page(pagenum)

            res = []
            for order in page.object_list:
                order_data = model_to_dict(order)
                order_data['username'] = order.cus_id.username
                order_data['orderlist'] = [
                    {
                        'dish_name': orderlist.dish.dish_name,
                        'orderlist_num': orderlist.ordlist_num
                    } for orderlist in order.orderlist_set.all()
                ]
                res.append(order_data)

            return JsonResponse({'code': 0, 'info': '查询成功', 'list': res, 'total': paginator.count})
        else:
            return JsonResponse({'code': 1, 'info': '提交数据缺失'})
    else:
        return JsonResponse({'code': 1, 'info': '请求方式错误'})


options = {
    'add': add,
    'update': update,
    'query': query
}


def handler(request):
    return request_handler(request, options)
