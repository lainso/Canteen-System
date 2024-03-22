# 2023-11-19
# 客户端自我管理，增（注册）在account.py中实现
import json
import traceback

from django.forms import model_to_dict
from django.http import JsonResponse

from customer.models import Customer
from lib.handler import request_handler


# 删除客户
def delete(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        cus_id = data.get('cus_id')
        if cus_id:
            try:
                Customer.objects.get(id=cus_id).delete()
                return JsonResponse({'code': 0, 'info': '删除成功'})
            except:
                return JsonResponse({'code': 1, 'info': '删除失败，无法找到该客户'})
        else:
            return JsonResponse({'code': 1, 'info': '删除失败，未提供客户ID'})
    else:
        return JsonResponse({'code': 1, 'info': '删除失败，禁止使用该方法提交'})


# 客户修改自己信息
def update(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        cus_id = data.get('cus_id')
        cus_data = data.get('cus_data')
        if cus_id:
            try:
                cus = Customer.objects.get(id=cus_id)
            except Customer.DoesNotExist:
                return JsonResponse({'code': 1, 'info': '修改失败，无法找到该客户'})

            if 'fname' in cus_data:
                cus.first_name = cus_data['fname']
            if 'tel' in cus_data:
                cus.cus_tel = cus_data['tel']
            if 'sex' in cus_data:
                cus.cus_sex = cus_data['sex']
            if 'birth' in cus_data:
                cus.cus_birth = cus_data['birth']
            if 'address' in cus_data:
                cus.cus_address = cus_data['address']
            cus.save()
            return JsonResponse({'code': 0, 'info': '修改成功'})
        else:
            return JsonResponse({'code': 1, 'info': '修改失败，未提供客户ID'})
    else:
        return JsonResponse({'code': 1, 'info': '修改失败，禁止使用该方法提交'})


#   客户查询自己的信息
def query(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        if username:
            try:
                cus = Customer.objects.get(username=username)
                res = model_to_dict(cus)
                return JsonResponse({'code': 0, 'info': '查询成功', 'list': res})
            except Customer.DoesNotExist:
                return JsonResponse({'code': 1, 'info': '查询失败，无法找到该客户'})
        else:
            return JsonResponse({'code': 1, 'info': f'错误：\n{traceback.format_exc()}'})


options = {
    'delete': delete,
    'update': update,
    'query': query
}


def handler(request):
    return request_handler(request, options)
