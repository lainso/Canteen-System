# 2323-12-12
# 管理员端:账户管理（管理员、客户、商户）-增删改查
# customer表
import json

from django.core.paginator import Paginator
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Q
from django.http import JsonResponse
from django_redis import get_redis_connection
import Canteen.settings as can_set
from customer.models import Customer
from lib.handler import request_handler


def add(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        fname = data.get('fname')
        sex = data.get('sex')
        tel = data.get('tel')
        birth = data.get('birth')
        address = data.get('address')
        is_active = data.get('is_active')
        usertype = data.get('usertype')
        if username and password and email and fname and is_active and usertype:
            new_user = Customer.objects.create_user(username=username, password=password,
                                                    email=email, is_superuser=0, cus_tel=tel,
                                                    first_name=fname, is_active=is_active,
                                                    cus_sex=sex, cus_birth=birth, cus_address=address,
                                                    usertype=usertype)
            get_redis_connection("default").delete(can_set.CacheKey.Cus_list)
            return JsonResponse({'code': 0, 'info': '账户添加成功，id为' + str(new_user.id)})
        else:
            return JsonResponse({'code': 1, 'info': '提交参数缺失'})
    else:
        return JsonResponse({'code': 1, 'info': '禁止使用该方法提交数据'})


def reset_shop_pass(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        if username:
            try:
                user = Customer.objects.get(username=username)
                if user is not None and user.usertype == 'shop':
                    user.set_password(can_set.SHOP_DEFAULT_PASS)
                    user.save()
                    return JsonResponse({'code': 0, 'info': '重置成功，新密码为：' + can_set.SHOP_DEFAULT_PASS})
                else:
                    return JsonResponse({'code': 1, 'info': '未找到合法用户，请检查'})
            except Exception as e:
                return JsonResponse({'code': 1, 'info': '重置密码失败：' + str(e)})
        else:
            return JsonResponse({'code': 1, 'info': '缺少必要数据'})
    else:
        return JsonResponse({'code': 1, 'info': '禁止使用该方法提交'})


def delete(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        cus_id = data.get('cus_id')
        if cus_id:
            try:
                Customer.objects.get(id=cus_id).delete()
                # 清除缓存
                get_redis_connection("default").delete(can_set.CacheKey.Cus_list)
                return JsonResponse({'code': 0, 'info': '删除成功'})
            except Customer.DoesNotExist:
                return JsonResponse({'code': 1, 'info': '删除失败，无法找到该客户'})
        else:
            return JsonResponse({'code': 1, 'info': '删除失败，未提供客户ID'})
    else:
        return JsonResponse({'code': 1, 'info': '删除失败，禁止使用该方法提交'})


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

            if 'email' in cus_data:
                cus.email = cus_data['email']
            if 'fname' in cus_data:
                cus.first_name = cus_data['fname']
            if 'sex' in cus_data:
                cus.cus_sex = cus_data['sex']
            if 'tel' in cus_data:
                cus.cus_tel = cus_data['tel']
            if 'birth' in cus_data:
                cus.cus_birth = cus_data['birth']
            if 'address' in cus_data:
                cus.cus_address = cus_data['address']
            if 'is_active' in cus_data:
                cus.is_active = cus_data['is_active']
            if 'usertype' in cus_data:
                cus.usertype = cus_data['usertype']
            cus.save()
            # 清除缓存
            get_redis_connection("default").delete(can_set.CacheKey.Cus_list)
            return JsonResponse({'code': 0, 'info': '修改成功'})
        else:
            return JsonResponse({'code': 1, 'info': '修改失败，未提供客户ID'})
    else:
        return JsonResponse({'code': 1, 'info': '修改失败，禁止使用该方法提交'})


# 引入Redis缓存方案
def query(request):
    if request.method == 'GET':
        keys = request.GET.get('keys', None)
        pagenum = request.GET.get('pagenum')
        pagesize = request.GET.get('pagesize')
        cacheField = f'{pagesize}|{pagenum}|{keys}'
        redis_conn = get_redis_connection('default')
        cacheObj = redis_conn.hget(can_set.CacheKey.Cus_list, cacheField)
        if cacheObj:
            obj = json.loads(cacheObj)
        else:
            cus_list = Customer.objects.all().order_by('-id')
            if keys:
                conditions = [Q(username__contains=con) for con in keys.split(' ') if con]
                querys = Q()
                for condi in conditions:
                    querys &= condi
                cus_list = cus_list.filter(querys)

            cus_list = cus_list.exclude(usertype='super')
            paginator = Paginator(cus_list, pagesize)
            page = paginator.get_page(pagenum)
            res = list(page.object_list.values())

            obj = {
                'code': 0,
                'info': '查询成功',
                'list': res,
                'total': paginator.count
            }

            cache_data = json.dumps(obj, cls=DjangoJSONEncoder)
            redis_conn.hset(can_set.CacheKey.Cus_list, cacheField, cache_data)
        return JsonResponse(obj)
    else:
        return JsonResponse({'code': 1, 'info': '查询失败，禁止使用该方法提交'})

def query_super(request):
    if request.method == 'GET':
        keys = request.GET.get('keys', None)
        pagenum = request.GET.get('pagenum')
        pagesize = request.GET.get('pagesize')

        cus_list = Customer.objects.all().order_by('-id').filter(usertype='super')
        if keys:
            conditions = [Q(username__contains=con) for con in keys.split(' ') if con]
            querys = Q()
            for condi in conditions:
                querys &= condi
            cus_list = cus_list.filter(querys)

        paginator = Paginator(cus_list, pagesize)
        page = paginator.get_page(pagenum)
        res = list(page.object_list.values())

        obj = {
            'code': 0,
            'info': '查询成功',
            'list': res,
            'total': paginator.count
        }
        return JsonResponse(obj)
    else:
        return JsonResponse({'code': 1, 'info': '查询失败，禁止使用该方法提交'})


options = {
    'query': query,
    'add': add,
    'delete': delete,
    'update': update,
    'querySuper': query_super,
    'resetShopPass': reset_shop_pass,
}


def handler(request):
    return request_handler(request, options)
