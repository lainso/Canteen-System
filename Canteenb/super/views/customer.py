# 2323-12-12
# 管理员端:账户管理（管理员、客户、商户）-增删改查
# customer表
import json

from django.core.paginator import Paginator
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
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


# 文件路径：canteen_backend/super/views/customer.py
# 定义了一个查询接口。require_http_methods表示需要使用GET方法进行调用。
@require_http_methods(['GET'])
def query(request):
    # 直接使用try包含整个接口的内容，以捕获所有发生的错误
    try:
        # 接收前端传递的keys，代表查询的过滤关键字，None表示默认为没有过滤
        keys = request.GET.get('keys', None)
        # 对分页页码和分页大小进行校验，以避免前端传递非法数据导致接口运行出错
        try:
            # 接收分页之后的页码，默认为1，即第一页
            pagenum = int(request.GET.get('pagenum', 1))
            # 接收分页大小，默认为10，表示每页显示10条数据
            pagesize = int(request.GET.get('pagesize', 10))
        # 捕获值错误，如果回传的参数无法转换为整数，则抛出ValueError异常
        except ValueError:
            # 返回Json错误信息，code为1表示失败，在info字段中对前端进行提示
            return JsonResponse({'code': 1, 'info': '参数错误，页码和页大小必须为整数'})
        # 对回传的参数进行进一步校验，规范分页页码必须大于0，且分页大小在1-100之间
        if pagenum <= 0 or not 1 <= pagesize <= 100:
            return JsonResponse({'code': 1, 'info': '页码或页大小超出允许范围'})

        # 缓存格式为key-value，这里定义key的值为分页大小|分页页码|过滤关键字
        cacheField = f'{pagesize}|{pagenum}|{keys}'
        # 获取缓存连接
        redis_conn = get_redis_connection('default')
        # 使用hget方法获取缓存内容，can_set为项目配置文件，CacheKey为其中的一个类，里面有Cus_list的定义
        # 尝试获取缓存的内容
        cacheObj = redis_conn.hget(can_set.CacheKey.Cus_list, cacheField)
        # 判断缓存是否命中
        if cacheObj:
            # 如果命中，则直接解缓存内容
            obj = json.loads(cacheObj)
        # 如果未命中，则执行数据库查询
        else:
            # 使用try包含数据库查询部分以捕获错误
            try:
                # 获取所有账户的内容，将用户类型为 'super' 的项排除，避免同级管理
                cus_list = Customer.objects.all().order_by('-id').exclude(usertype='super')
                if keys:
                    # 如果存在过滤关键字则使用Q方法进行过滤
                    cus_list = cus_list.filter(
                        Q(username__icontains=keys) |
                        Q(email__icontains=keys)
                    )
                # 将得到的结果进行分页处理，然后返回分页后数据
                paginator = Paginator(cus_list, pagesize)
                page = paginator.get_page(pagenum)
                res = list(page.object_list.values())
                # 构造结果数据集
                obj = {
                    'code': 0,
                    'info': '查询成功',
                    'list': res,
                    'total': paginator.count
                }
                # 格式化结果集
                cache_data = json.dumps(obj, cls=DjangoJSONEncoder)
                # 将结果缓存到redis中
                redis_conn.hset(can_set.CacheKey.Cus_list, cacheField, cache_data)
            # 捕获数据库查询中发生的错误并返回
            except Exception as e:
                return JsonResponse({'code': 1, 'info': '数据库查询错误' + str(e)})
        # 将结果集返回给前端
        return JsonResponse(obj)
    # 捕获接口查询中发生的错误并返回
    except Exception as e:
        return JsonResponse({'code': 1, 'info': '接口错误' + str(e)})


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
