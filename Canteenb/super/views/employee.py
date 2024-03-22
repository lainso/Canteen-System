# 2023-12-13
# 管理员端：员工管理
import json

from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django_redis import get_redis_connection
import Canteen.settings as can_set
from lib.handler import request_handler
from shop.models import Shop, Employee


# 删除员工
def delete(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        emp_id = data.get('emp_id')
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
                emp = Employee.objects.get(id=emp_id)
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


# 根据员工姓名模糊查询员工
def query(request):
    if request.method == 'GET':
        keys = request.GET.get('keys', None)
        pagenum = request.params['pagenum']
        pagesize = request.params['pagesize']
        if pagenum and pagesize:
            try:
                emp_list = Employee.objects.all().order_by('-id').select_related('emp_shop_id')
                if keys:
                    conditions = [Q(emp_name__contains=con) for con in keys.split(' ') if con]
                    querys = Q()
                    for condi in conditions:
                        querys &= condi
                    emp_list = emp_list.filter(querys)
                paginator = Paginator(emp_list, pagesize)

                page = paginator.get_page(pagenum)
                res = list(page.object_list.values('id', 'emp_name', 'emp_shop_id__shop_name', 'emp_number', 'emp_tel',
                                                   'emp_role', 'emp_condition'))
                return JsonResponse({'code': 0, 'info': '查询成功', 'list': res, 'total': paginator.count})
            except Exception as e:
                return JsonResponse({'code': 1, 'info': '查询失败：' + str(e)})
        else:
            return JsonResponse({'code': 1, 'info': '查询失败，未提供分页参数'})
    else:
        return JsonResponse({'code': 1, 'info': '查询失败，禁止使用该方法提交'})


options = {
    'query': query,
    'delete': delete,
    'update': update
}


def handler(request):
    return request_handler(request, options)
