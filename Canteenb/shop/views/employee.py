# 23-11-25
# 商户端：员工管理
import json

from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django_redis import get_redis_connection
import Canteen.settings as can_set
from customer.models import Customer
from lib.handler import request_handler
from shop.models import Shop, Employee


# 添加员工到商户
def add(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        emp_name = data.get('emp_name')
        emp_number = data.get('emp_number')
        emp_tel = data.get('emp_tel')
        emp_condition = data.get('emp_condition')
        emp_role = data.get('emp_role')
        if username and emp_name and emp_tel and emp_condition and emp_role and emp_number:
            try:
                user = Customer.objects.get(username=username)
                shop = Shop.objects.get(shop_cus=user.id)
                if shop:
                    new_emp = Employee.objects.create(emp_name=emp_name, emp_tel=emp_tel, emp_number=emp_number,
                                                      emp_condition=emp_condition, emp_role=emp_role, emp_shop=shop)
                    get_redis_connection("default").delete(can_set.CacheKey.Emp_list)
                    return JsonResponse({'code': 0, 'info': '员工添加成功，id为' + str(new_emp.id)})
                else:
                    return JsonResponse({'code': 1, 'info': '找不到商户，请检查'})
            except Exception as e:
                return JsonResponse({'code': 1, 'info': '添加员工失败：' + str(e)})
        else:
            return JsonResponse({'code': 1, 'info': '提交数据缺失'})
    else:
        return JsonResponse({'code': 1, 'info': '添加失败，禁止使用该方法提交'})


def join_by_code(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        emp_name = data.get('emp_name')
        emp_tel = data.get('emp_tel')
        shop_pass = data.get('shop_pass')

        if emp_name and emp_tel and shop_pass:
            try:
                shop = Shop.objects.get(shop_pass=shop_pass)
                if shop:
                    Employee.objects.create(emp_name=emp_name, emp_tel=emp_tel, emp_number='暂未分配',
                                            emp_condition='新加入', emp_role='暂未分配', emp_shop=shop)
                    get_redis_connection("default").delete(can_set.CacheKey.Emp_list)
                    return JsonResponse({'code': 0, 'info': '员工加入商户成功！'})
                else:
                    return JsonResponse({'code': 1, 'info': '找不到商户，请检查'})
            except Shop.DoesNotExist:
                return JsonResponse({'code': 1, 'info': '加入失败，请检查邀请码是否正确！'})
            except Exception as e:
                return JsonResponse({'code': 1, 'info': '加入失败：' + str(e)})
        else:
            return JsonResponse({'code': 1, 'info': '提交数据缺失'})
    else:
        return JsonResponse({'code': 1, 'info': '添加失败，禁止使用该方法提交'})


# 删除员工
def delete(request):
    if request.method == 'POST':
        emp_id = request.params['emp_id']
        if emp_id:
            try:
                Employee.objects.get(id=emp_id).delete()
                get_redis_connection("default").delete(can_set.CacheKey.Emp_list)
                return JsonResponse({'code': 0, 'info': '员工删除成功'})
            except Employee.DoesNotExist:
                return JsonResponse({'code': 1, 'info': '删除失败'})
        else:
            return JsonResponse({'code': 1, 'info': '删除失败，未提供员工ID'})
    else:
        return JsonResponse({'code': 1, 'info': '删除失败，禁止使用该方法提交'})


# 修改员工信息
def update(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        emp_id = data.get('emp_id')
        emp_data = data.get('emp_data')
        if emp_id:
            try:
                emp = Employee.objects.get(emp_id=emp_id)
            except Employee.DoesNotExist:
                return JsonResponse({'code': 1, 'info': '修改失败，无法找到该员工'})

            if 'emp_name' in emp_data:
                emp.emp_name = emp_data['emp_name']
            if 'emp_tel' in emp_data:
                emp.emp_tel = emp_data['emp_tel']
            if 'emp_number' in emp_data:
                emp.emp_number = emp_data['emp_number']
            if 'emp_condition' in emp_data:
                emp.emp_condition = emp_data['emp_condition']
            if 'emp_role' in emp_data:
                emp.emp_role = emp_data['emp_role']
            emp.save()
            get_redis_connection("default").delete(can_set.CacheKey.Emp_list)
            return JsonResponse({'code': 0, 'info': '员工修改成功'})
        else:
            return JsonResponse({'code': 1, 'info': '修改失败，未提供员工ID'})
    else:
        return JsonResponse({'code': 1, 'info': '修改失败，禁止使用该方法提交'})


# 根据员工姓名模糊查询员工，否则返回所有员工信息，引入redis缓存
def query(request):
    if request.method == 'GET':
        try:
            keys = request.GET.get('keys', None)
            pagenum = request.params['pagenum']
            pagesize = request.params['pagesize']
            username = request.params['username']

            cacheField = f'{pagesize}|{pagenum}|{keys}'
            redis_conn = get_redis_connection('default')
            cacheObj = redis_conn.hget(can_set.CacheKey.Emp_list, cacheField)
            if cacheObj:
                obj = json.loads(cacheObj)
            else:
                user = Customer.objects.get(username=username)
                shop = Shop.objects.get(shop_cus=user.id)
                emp_list = Employee.objects.all().order_by('-id').filter(emp_shop=shop.id)
                if keys:
                    conditions = [Q(emp_name__contains=con) for con in keys.split(' ') if con]
                    querys = Q()
                    for condi in conditions:
                        querys &= condi
                    emp_list = emp_list.filter(querys)
                paginator = Paginator(emp_list, pagesize)
                page = paginator.get_page(pagenum)
                res = list(page.object_list.values())

                obj = {'code': 0, 'info': '查询成功', 'list': res, 'total': paginator.count}
                redis_conn.hset(can_set.CacheKey.Emp_list, cacheField, json.dumps(obj))

            return JsonResponse(obj)

        except Exception as e:
            return JsonResponse({'code': 1, 'info': '查询失败：' + str(e)})
    else:
        return JsonResponse({'code': 1, 'info': '查询失败，禁止使用该方法提交'})


options = {
    'query': query,
    'add': add,
    'delete': delete,
    'update': update
}


def handler(request):
    return request_handler(request, options)
