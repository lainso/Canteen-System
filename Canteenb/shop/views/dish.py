# 2023-11-28
# 商户端：菜品管理
import json

from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse

from customer.models import Customer
from lib.handler import request_handler
from shop.models import Shop, Dish


# 添加菜品到商户
def add(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        dish_name = data.get('dish_name')
        dish_price = data.get('dish_price')
        dish_des = data.get('dish_des', None)
        dish_img = data.get('dish_img', None)
        username = data.get('username')
        if dish_name and dish_price and username:
            try:
                user = Customer.objects.get(username=username)
                shop = Shop.objects.get(shop_cus=user.id)
                if shop:
                    new_dish = Dish.objects.create(dish_name=dish_name, dish_price=dish_price,
                                                   dish_des=dish_des, dish_img=dish_img, dish_shop=shop)
                    return JsonResponse({'code': 0, 'info': '菜品添加成功，id为' + str(new_dish.id)})
                else:
                    return JsonResponse({'code': 1, 'info': '商户不存在'})
            except Exception as e:
                return JsonResponse({'code': 1, 'info': '添加菜品失败：' + str(e)})
        else:
            return JsonResponse({'code': 1, 'info': '提交数据缺失'})
    else:
        return JsonResponse({'code': 1, 'info': '添加失败，禁止使用该方法提交'})


# 删除菜品
def delete(request):
    if request.method == 'POST':
        dish_id = request.params['dish_id']
        if dish_id:
            try:
                Dish.objects.get(id=dish_id).delete()
                return JsonResponse({'code': 0, 'info': '菜品删除成功！'})
            except Dish.DoesNotExist:
                return JsonResponse({'code': 1, 'info': '删除失败，无法找到该菜品'})
        else:
            return JsonResponse({'code': 1, 'info': '删除失败，未提供菜品ID'})
    else:
        return JsonResponse({'code': 1, 'info': '删除失败，禁止使用该方法提交'})


# 修改菜品信息
def update(request):
    if request.method == 'POST':
        dish_id = request.params['dish_id']
        dish_data = request.params['dish_data']
        if dish_id:
            try:
                dish = Dish.objects.get(dish_id=dish_id)
            except Dish.DoesNotExist:
                return JsonResponse({'code': 1, 'info': '修改失败，无法找到该菜品'})

            if 'dish_name' in dish_data:
                dish.dish_name = dish_data['dish_name']
            if 'dish_des' in dish_data:
                dish.dish_des = dish_data['dish_des']
            if 'dish_price' in dish_data:
                dish.dish_price = dish_data['dish_price']
            if 'dish_img' in dish_data:
                dish.dish_img = dish_data['dish_img']
            dish.save()
            return JsonResponse({'code': 0, 'info': '菜品修改成功'})
        else:
            return JsonResponse({'code': 1, 'info': '修改失败，未提供菜品ID'})
    else:
        return JsonResponse({'code': 1, 'info': '修改失败，禁止使用该方法提交'})


#   商户模糊查询自己的菜品
@require_http_methods(["GET"])
def query(request):
    try:
        keys = request.GET.get('keys', None)
        pagenum = request.GET.get('pagenum')
        pagesize = request.GET.get('pagesize')
        username = request.GET.get('username')

        # 输入检查和转换
        if not all([username, pagesize, pagenum]):
            return JsonResponse({'code': 1, 'info': '查询失败，有缺失的参数未提交'})
        try:
            pagesize = int(pagesize)
            pagenum = int(pagenum)
        except ValueError:
            return JsonResponse({'code': 1, 'info': '查询失败，无效的分页参数'})

        # 数据库查询及异常处理
        try:
            user = Customer.objects.get(username=username)
            shop = Shop.objects.get(shop_cus=user.id)
        except ObjectDoesNotExist:
            return JsonResponse({'code': 1, 'info': '用户或商店不存在'})
        
        # 查询逻辑
        dish_list = Dish.objects.filter(dish_shop=shop.id).order_by('-id')
        if keys:
            conditions = [Q(dish_name__contains=con) for con in keys.split(' ') if con]
            querys = Q()
            for condi in conditions:
                querys &= condi
            dish_list = dish_list.filter(querys)
            
        paginator = Paginator(dish_list, pagesize)
        
        # 分页处理
        if pagenum > paginator.num_pages:
            pagenum = paginator.num_pages
        page = paginator.get_page(pagenum)
        
        res = list(page.object_list.values())
        
        return JsonResponse({'code': 0, 'info': '查询成功', 'list': res, 'total': paginator.count})
    except Exception as e:
        return JsonResponse({'code': 1, 'info': '查询失败，服务器内部错误：' + str(e)})

options = {
    'add': add,
    'delete': delete,
    'update': update,
    'query': query
}


def handler(request):
    return request_handler(request, options)
