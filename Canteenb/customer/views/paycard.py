# 2023-11-20
# 顾客端 | 支付卡管理：申请、激活、注销、查询
from datetime import datetime
import json
import random
import string
import time
from decimal import Decimal

from django.core.cache import cache
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.forms import model_to_dict
from django.http import JsonResponse

import Canteen.settings as can_set
from comment.models import Promotions
from customer.models import Paycard, Customer
from lib.handler import request_handler


# 申请支付卡
def register(request):
    if request.method == 'POST':
        # 生成总共16位的唯一支付卡号，添加时间戳
        card_number = str(int(time.time())) + ''.join(random.sample(string.ascii_letters + string.digits, 6))
        data = json.loads(request.body)
        username = data.get('username')
        if username is not None:
            # 根据username获取用户名字和邮箱
            customer = Customer.objects.get(username=username)
            fname = customer.first_name
            email = customer.email
            card = Paycard.objects.create(card_number=card_number, cus_id_id=customer.id, card_balance=0,
                                          card_condition='未激活')

            mix_code = str(card.id) + 'X' + ''.join([str(random.randint(0, 9)) for _ in range(5)])
            code = mix_code.split("X")[1]
            cache.set(str(card.id), code, 1800)

            # 邮件激活
            sub = '【餐饮系统】支付卡激活邮件'
            msg = '''
                <div style="
                background-color: #f6f8fb;
                margin: auto;
                text-align: center;
                border-radius: 20px;">
                    <br>
                    <div style="display: flex; justify-content: center;">
                        <span style="font-size: 2.3rem; font-weight: bold;">餐 饮 系 统</span>
                    </div>
                    <p style="font-weight: lighter; font-size: 15px;">支 付 卡 激 活 </p>
                    <p>尊敬的 {}<br>欢迎使用系统支付卡系统</p>
                    <div>
                        <p target="_blank">您的激活码为：<span style="font-weight: bolder; ">{}</span></p>
                    </div>
                    <br>
                </div>
            '''.format(fname, mix_code)
            send_mail(subject=sub, message=msg, from_email=can_set.EMAIL_HOST_USER, recipient_list=[email, ],
                      html_message=msg)
            return JsonResponse({'code': 0, 'msg': '发送激活邮件成功'})
        else:
            return JsonResponse({'code': 1, 'msg': '未获取到用户id'})
    else:
        return JsonResponse({'code': 2, 'msg': '请使用POST提交'})


# 激活支付卡
def active(request):
    data = json.loads(request.body)
    code = data.get('code')
    card_id = data.get('card_id')
    if cache.get(card_id) == code:
        card = Paycard.objects.get(id=card_id)
        card.card_condition = '已激活'
        card.save()
        # 删除session
        cache.delete(card_id)

        return JsonResponse({'code': 0, 'msg': '激活成功'})
    else:
        return JsonResponse({'code': 1, 'msg': '激活失败，卡号获取失败'})


# 注销支付卡
def delete(request):
    data = json.loads(request.body)
    card_number = data.get('card_number')
    if card_number is not None:
        card = Paycard.objects.get(card_number=card_number)
        card.delete()
        return JsonResponse({'code': 0, 'msg': '注销成功'})
    else:
        return JsonResponse({'code': 1, 'msg': '注销失败，卡号获取失败'})


# 查询支付卡信息
def query(request):
    username = request.GET.get('username')
    if username is not None:
        try:
            customer = Customer.objects.get(username=username)
            card = Paycard.objects.get(cus_id_id=customer.id)
            res = model_to_dict(card)
            return JsonResponse({'code': 0, 'msg': '查询成功', 'data': res})
        except Customer.DoesNotExist:
            return JsonResponse({'code': 1, 'msg': '查询失败，未查询到该用户'})
        except Paycard.DoesNotExist:
            return JsonResponse({'code': 1, 'msg': '查询失败，未查询到卡信息'})
    else:
        return JsonResponse({'code': 1, 'msg': '查询失败，未获取到用户名'})


#   支付卡充值消费
def update(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        card_number = data.get('card_number')
        money = data.get('money')
        promo_code_input = data.get('code')
        current_time = datetime.utcnow()

        if card_number is None:
            return JsonResponse({'code': 1, 'msg': '失败，未获取到卡号'})

        try:
            card = Paycard.objects.get(card_number=card_number)  # 查找支付卡信息
            original_money = Decimal(money)  # 保存原始充值金额

            # 检查是否有优惠码，并尝试应用
            if promo_code_input:
                try:
                    # 获取优惠码信息
                    promotion = Promotions.objects.get(promo_code=promo_code_input)

                    # 手动解析优惠期开始和结束时间
                    promo_start = datetime.fromisoformat(promotion.promo_start.rstrip('Z'))
                    promo_end = datetime.fromisoformat(promotion.promo_end.rstrip('Z'))

                    if promo_start <= current_time <= promo_end:
                        # 优惠码有效，应用优惠倍数
                        money = original_money * promotion.promo_multiple
                    else:
                        # 优惠码无效或不在有效期
                        print('优惠码不在有效期内，将按原始金额执行充值。')

                except ObjectDoesNotExist:
                    # 优惠码不存在
                    print('提供的优惠码不存在，将按原始金额执行充值。')

            card.card_balance += Decimal(money)
            card.save()
            return JsonResponse({'code': 0, 'msg': '成功'})

        except ObjectDoesNotExist:
            return JsonResponse({'code': 1, 'msg': '失败，未找到对应的卡信息'})
    else:
        return JsonResponse({'code': 1, 'msg': '请求方法非法'})


options = {
    'register': register,
    'active': active,
    'delete': delete,
    'query': query,
    'update': update
}


def handler(request):
    return request_handler(request, options)
