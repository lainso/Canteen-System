# 2023-12-13
# 管理员端：菜品管理
import json

from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from lib.handler import request_handler
from shop.models import Dish


# 删除菜品
def delete(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        dish_id = data.get('dish_id')
        if dish_id:
            try:
                Dish.objects.get(id=dish_id).delete()
                return JsonResponse({'code': 0, 'info': '菜品删除成功'})
            except Dish.DoesNotExist:
                return JsonResponse({'code': 1, 'info': '删除失败，无法找到该菜品'})
        else:
            return JsonResponse({'code': 1, 'info': '删除失败，未提供菜品ID'})
    else:
        return JsonResponse({'code': 1, 'info': '删除失败，禁止使用该方法提交'})


# 修改菜品信息
def update(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        dish_id = data.get('dish_id')
        dish_data = data.get('dish_data')
        print(dish_id, dish_data)
        if dish_id:
            try:
                dish = Dish.objects.get(id=dish_id)
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


#   模糊查询菜品
def query(request):
    if request.method == 'GET':
        keys = request.GET.get('keys', None)
        pagenum = request.GET.get('pagenum')  # 如果你是通过GET提交的参数，这里应该使用GET而不是params
        pagesize = request.GET.get('pagesize')  # 注意，GET参数通常是字符串需要转换成整数

        try:
            # 将字符串参数转换为整数
            pagenum = int(pagenum)
            pagesize = int(pagesize)
        except (ValueError, TypeError):
            return JsonResponse({'code': 1, 'info': '查询失败，分页参数应为整数'})

        if pagesize and pagenum:
            # 在查询Dish的时候就将对应的Shop提前获取，避免后续的逐个查询
            dish_list = Dish.objects.select_related('dish_shop').order_by('-id')
            if keys:
                conditions = [Q(dish_name__contains=con) for con in keys.split(' ') if con]
                querys = Q()
                for condi in conditions:
                    querys &= condi
                dish_list = dish_list.filter(querys)
            paginator = Paginator(dish_list, pagesize)
            page = paginator.get_page(pagenum)

            # 获取相关的dishes，并且增加shop_name到结果中
            res = []
            for dish in page.object_list:
                dish_data = {
                    'id': dish.id,
                    'dish_name': dish.dish_name,
                    'dish_des': dish.dish_des,
                    'dish_price': dish.dish_price,
                    'dish_img': dish.dish_img,
                    'dish_shop': dish.dish_shop.shop_name,
                }
                res.append(dish_data)

            return JsonResponse({'code': 0, 'info': '查询成功', 'list': res, 'total': paginator.count})
        else:
            return JsonResponse({'code': 1, 'info': '查询失败，有缺失的参数未提交'})
    else:
        return JsonResponse({'code': 1, 'info': '查询失败，禁止使用该方法提交'})


options = {
    'delete': delete,
    'update': update,
    'query': query
}


def handler(request):
    return request_handler(request, options)
