# 2023-11-20
# 客户端订单管理：查询订单信息
import json

from django.core import serializers
from django.db.models import Prefetch
from django.http import JsonResponse
from django.core.paginator import Paginator

from customer.models import Customer
from shop.models import Order, Shop


# 顾客查询关于自己的订单
def query_orders(request):
    username = request.GET.get('username')
    start_time = request.GET.get('start_time', None)
    end_time = request.GET.get('end_time', None)
    pagesize = int(request.GET.get('pagesize', 5))
    pagenum = int(request.GET.get('pagenum', 1))

    if username and pagesize and pagenum:
        customer = Customer.objects.get(username=username)
        # 预先提取Shop信息
        shop_queryset = Shop.objects.all().order_by('-id')
        order_list = Order.objects.filter(cus_id_id=customer.id).prefetch_related(Prefetch('ord_shop', queryset=shop_queryset))

        if start_time and end_time:
            order_list = order_list.filter(ord_time__range=(start_time, end_time))

        paginator = Paginator(order_list, pagesize)
        page = paginator.get_page(pagenum)

        # 手动构建数据，包括shop_name字段
        data = []
        for order in page:
            order_data = {
                'id': order.id,
                'ord_shop': order.ord_shop_id,
                'shop_name': order.ord_shop.shop_name,
                'ord_time': order.ord_time,
                'ord_number': order.ord_number,
                'ord_money': order.ord_money,
                'ord_condition': order.ord_condition,
            }
            data.append(order_data)

        return JsonResponse({
            'code': 0,
            'msg': '查询成功',
            'data': data,
            'total': paginator.count
        })
    else:
        return JsonResponse({'code': 1, 'msg': '查询失败'})
