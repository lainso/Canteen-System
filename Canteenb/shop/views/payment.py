# 2023-12-12
# 商戶端：支付信息管理-創建
import json
import random
import string
import time

from django.http import JsonResponse
from comment.models import Payment
from shop.models import Order


def add(request):
    if request.method == 'POST':
        # 生成18位支付号
        pay_num = str(int(time.time())) + ''.join(random.sample(string.ascii_letters + string.digits, 8))
        pay_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        data = json.loads(request.body)
        pay_money = data.get('pay_money')
        pay_way = data.get('pay_way')
        ord_id = data.get('ord_id')
        try:
            order = Order.objects.get(id=ord_id)
            if order:
                if ord_id and pay_money:
                    new_pay = Payment.objects.create(pay_num=pay_num, pay_time=pay_time,
                                                     pay_money=pay_money, pay_way=pay_way, ord_id=order)
                    new_pay.save()
                    return JsonResponse({'code': 0, 'info': '支付记录添加成功，id为' + str(new_pay.id)})
                else:
                    return JsonResponse({'code': 1, 'info': '缺少必要参数'})
        except Order.DoesNotExist:
            return JsonResponse({'code': 1, 'info': '添加支付信息失败，订单不存在'})
    else:
        return JsonResponse({'code': 1, 'info': '禁止使用该方法提交数据'})
