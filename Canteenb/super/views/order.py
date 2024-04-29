# 2023-12-13
# 管理员端：订单管理
import json

from django.core.paginator import Paginator
from django.db import IntegrityError
from django.db.models import Q
from django.forms import model_to_dict
from django.http import JsonResponse

from lib.handler import request_handler
from shop.models import Order, OrderList


def delete(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        ord_num = data.get('ord_number')
        try:
            # 首先删除依赖于Order对象的OrderList对象
            OrderList.objects.filter(ord_number=ord_num).delete()
            # 然后删除Order对象
            order = Order.objects.get(ord_number=ord_num)
            order.delete()
            return JsonResponse({'code': 0, 'info': '订单删除成功'})
        except Order.DoesNotExist:
            return JsonResponse({'code': 1, 'info': '没有找到对应的订单'})
        except IntegrityError:
            return JsonResponse({'code': 1, 'info': '无法删除：系统中仍存在相关订单的记录'})
        except Exception as e:
            return JsonResponse({'code': 1, 'info': '订单删除失败：' + str(e)})
    else:
        return JsonResponse({'code': 1, 'info': '禁止使用该方法提交数据'})


def update(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        ord_number = data.get('ord_number')
        ord_condition = data.get('ord_condition')
        if ord_number and ord_condition:
            try:
                order = Order.objects.get(ord_number=ord_number)
                order.ord_condition = '管理员修改为：' + ord_condition
                order.save()
                return JsonResponse({'code': 0, 'info': '订单修改成功'})
            except Exception as e:
                return JsonResponse({'code': 1, 'info': '订单修改失败：' + str(e)})
        else:
            return JsonResponse({'code': 1, 'info': '提交数据缺失'})
    else:
        return JsonResponse({'code': 1, 'info': '请求方式错误'})


#  查询订单
def query(request):
    if request.method == 'GET':
        keys = request.GET.get('keys', None)
        pagenum = request.GET.get('pagenum', None)
        pagesize = request.GET.get('pagesize', None)

        if pagesize and pagenum:
            order_list = Order.objects.select_related('cus_id', 'ord_shop').all().order_by('-id')

            if keys:
                conditions = [Q(ord_time__contains=con) for con in keys.split(' ') if con]
                querys = Q()
                for condi in conditions:
                    querys &= condi
                order_list = order_list.filter(querys)

            paginator = Paginator(order_list, pagesize)
            page = paginator.get_page(pagenum)

            # 创建一个新列表，用来存储包含额外信息的订单数据
            res = []
            for order in page.object_list:
                order_data = model_to_dict(order)  # 使用model_to_dict来获取模型的数据字典
                # 添加customer的username
                order_data['username'] = order.cus_id.username
                # 添加shop的shop_name
                order_data['shop_name'] = order.ord_shop.shop_name
                # 创建一个列表来存储orderlist中每个菜品的信息
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
    'delete': delete,
    'update': update,
    'query': query
}


def handler(request):
    return request_handler(request, options)
