# 2023-12-17
# 管理员端：商户管理
import json
import random
import string
import time

from django.core.paginator import Paginator
from django.db import transaction
from django.db.models import Q
from django.http import JsonResponse
from django_redis import get_redis_connection
import Canteen.settings as can_set

from customer.models import Customer
from lib.handler import request_handler
from shop.models import Shop


def add(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # 获取客户信息
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        fname = data.get('fname')
        address = data.get('address')
        is_active = data.get('is_active')
        # 获取商户信息
        shop_name = data.get('shop_name')
        shop_tel = data.get('shop_tel')
        shop_head = data.get('shop_head', None)
        shop_pass = data.get('shop_pass')

        # 检查必须的字段
        if all([username, password, email, fname, is_active, shop_name, shop_tel, shop_pass]):
            try:
                with transaction.atomic():  # 确保两个对象都创建成功
                    # 创建客户
                    new_customer = Customer.objects.create_user(
                        username=username, password=password, email=email, is_superuser=0, cus_tel=shop_tel,
                        first_name=fname, is_active=is_active, cus_address=address, usertype='shop')
                    # 生成商户编号
                    shop_number = str(int(time.time())) + ''.join(
                        random.sample(string.ascii_letters + string.digits, 9))
                    # 创建商户
                    new_shop = Shop.objects.create(
                        shop_name=shop_name, shop_number=shop_number, shop_cus=new_customer,
                        shop_tel=shop_tel, shop_head=shop_head, shop_pass=shop_pass)

                    # 清除缓存（如果你有一个名为can_set的helper模块并且其中有适用的CacheKey）
                    get_redis_connection("default").delete(can_set.CacheKey.Cus_list)  # 假设你有一个这样的缓存key
                    # 返回成功信息
                    return JsonResponse({
                        'code': 0,
                        'info': f'账户和商户添加成功，customer_id为{new_customer.id}, shop_id为{new_shop.id}'
                    })
            except Exception as e:
                return JsonResponse({'code': 1, 'info': '发生错误：' + str(e)})
        else:
            return JsonResponse({'code': 1, 'info': '提交参数缺失'})
    else:
        return JsonResponse({'code': 1, 'info': '禁止使用该方法提交数据'})


def delete(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        shop_id = data.get('shop_id')
        if shop_id:
            try:
                with transaction.atomic():  # 使用事务确保一致性
                    # 获取商户实例
                    shop = Shop.objects.select_related('shop_cus').get(id=shop_id)
                    customer_id = shop.shop_cus.id

                    # 删除商户
                    shop.delete()

                    # 删除关联的用户
                    Customer.objects.filter(id=customer_id).delete()
                    get_redis_connection("default").delete(can_set.CacheKey.Cus_list)
                    return JsonResponse({'code': 0, 'info': '商户和客户删除成功'})
            except Shop.DoesNotExist:
                return JsonResponse({'code': 1, 'info': '删除失败，无法找到该商户'})
            except Exception as e:
                return JsonResponse({'code': 1, 'info': '发生错误：' + str(e)})
        else:
            return JsonResponse({'code': 1, 'info': '删除失败，未提供商户ID'})
    else:
        return JsonResponse({'code': 1, 'info': '删除失败，禁止使用该方法提交'})


def update(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        shop_id = data.get('shop_id')
        shop_data = data.get('shop_data')
        if shop_id:
            try:
                shop = Shop.objects.get(id=shop_id)
            except Shop.DoesNotExist:
                return JsonResponse({'code': 1, 'info': '修改失败，无法找到该商户'})

            if 'shop_name' in shop_data:
                shop.shop_name = shop_data['shop_name']
            if 'shop_tel' in shop_data:
                shop.shop_tel = shop_data['shop_tel']
            if 'shop_head' in shop_data:
                shop.shop_head = shop_data['shop_head']
            if 'shop_pass' in shop_data:
                shop.shop_pass = shop_data['shop_pass']
            shop.save()
            return JsonResponse({'code': 0, 'info': '商户信息修改成功'})
        else:
            return JsonResponse({'code': 1, 'info': '修改失败，未提供商户ID'})
    else:
        return JsonResponse({'code': 1, 'info': '修改失败，禁止使用该方法提交'})


def query(request):
    if request.method == 'GET':
        keys = request.GET.get('keys', None)
        pagenum = request.GET.get('pagenum', None)  # 应为request.GET.get
        pagesize = request.GET.get('pagesize', None)  # 应为request.GET.get

        if pagesize and pagenum:
            try:
                pagenum = int(pagenum)
                pagesize = int(pagesize)
            except ValueError:
                return JsonResponse({'code': 1, 'info': '查询失败，pagenum和pagesize需要为数字'})

            # 进行联合查询，同时选择相应的Customer信息
            shop_list = Shop.objects.select_related('shop_cus').all().order_by('-id')
            if keys:
                conditions = [Q(shop_name__contains=con) for con in keys.split(' ') if con]
                querys = Q()
                for condi in conditions:
                    querys = querys & condi
                shop_list = shop_list.filter(querys)
            paginator = Paginator(shop_list, pagesize)
            page = paginator.get_page(pagenum)

            # 构造包含customer.username的返回数据
            res = [
                {
                    'id': shop.id,
                    'shop_name': shop.shop_name,
                    'shop_tel': shop.shop_tel,
                    'shop_head': shop.shop_head,
                    'shop_pass': shop.shop_pass,
                    'shop_number': shop.shop_number,
                    'shop_cus_id': shop.shop_cus_id,
                    'shop_cus': shop.shop_cus.username  # 假设Customer模型中有一个username字段
                } for shop in page.object_list
            ]
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
