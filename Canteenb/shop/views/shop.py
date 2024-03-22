# 2023-11-24
# 商户端：商户自我管理
import json
import traceback

from django.db import transaction
from django.forms import model_to_dict
from django.http import JsonResponse

from customer.models import Customer
from lib.handler import request_handler
from shop.models import Shop


# 商户更新自己信息
def update(request):
    if request.method == 'POST':
        try:
            username = request.params['username']
            data = request.params['data']
            if not username:
                return JsonResponse({'code': 1, 'info': '修改失败，未提供商户用户名'})

            with transaction.atomic():
                try:
                    user = Customer.objects.select_for_update().get(username=username)
                    shop = Shop.objects.select_for_update().get(shop_cus=user.id)
                    updated_fields_user = []
                    updated_fields_shop = []

                    if 'shop_name' in data:
                        shop.shop_name = data['shop_name']
                        user.first_name = data['shop_name']
                        updated_fields_shop.append('shop_name')
                        updated_fields_user.append('first_name')

                    if 'shop_tel' in data:
                        shop.shop_tel = data['shop_tel']
                        user.cus_tel = data['shop_tel']
                        updated_fields_shop.append('shop_tel')
                        updated_fields_user.append('cus_tel')

                    if 'shop_head' in data:
                        shop.shop_head = data['shop_head']
                        updated_fields_shop.append('shop_head')

                    if 'shop_pass' in data:
                        shop.shop_pass = data['shop_pass']
                        updated_fields_shop.append('shop_pass')

                    if 'email' in data:
                        user.email = data['email']
                        updated_fields_user.append('email')

                    if 'address' in data:
                        user.cus_address = data['address']
                        updated_fields_user.append('cus_address')

                    user.save(update_fields=updated_fields_user)
                    shop.save(update_fields=updated_fields_shop)

                    return JsonResponse({'code': 0, 'info': '修改成功'})

                except Customer.DoesNotExist:
                    return JsonResponse({'code': 1, 'info': '修改失败，无法找到该用户'})
                except Shop.DoesNotExist:
                    return JsonResponse({'code': 1, 'info': '修改失败，无法找到该商户'})

        except KeyError as e:
            return JsonResponse({'code': 1, 'info': f'修改失败，缺少参数: {e}'})

        except Exception as e:
            return JsonResponse({'code': 1, 'info': f'服务器错误: {e}'})
    else:
        return JsonResponse({'code': 1, 'info': '修改失败，禁止使用该方法提交'})


# 商户查询自己信息
def query(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        try:
            user = Customer.objects.get(username=username)
            shop = Shop.objects.get(shop_cus=user.id)
            res = model_to_dict(user)
            res.update(model_to_dict(shop))
            return JsonResponse({'code': 0, 'data': res, 'info': '查询成功！'})
        except Shop.DoesNotExist:
            return JsonResponse({'code': 1, 'info': '查询失败，无法找到该商户'})
    else:
        return JsonResponse({'code': 1, 'info': '修改失败，禁止使用该方法提交'})


options = {
    'query': query,
    'update': update
}


def handler(request):
    return request_handler(request, options)
