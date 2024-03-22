import json

from django.http import JsonResponse

from customer.models import Customer, Paycard


def update(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        money = data.get('money')

        if username and money:
            try:
                customer = Customer.objects.get(username=username)
                paycard = Paycard.objects.get(cus_id=customer)
                paycard.card_balance = paycard.card_balance - money
                if paycard.card_balance > 0:
                    paycard.save()
                    return JsonResponse({'code': 0, 'info': '支付卡扣费成功'})
                else:
                    return JsonResponse({'code': 1, 'info': '支付卡余额不足'})
            except Customer.DoesNotExist:
                return JsonResponse({'code': 1, 'info': '未找到用户，请检查'})
            except Paycard.DoesNotExist:
                return JsonResponse({'code':1, 'info': '用户未开通支付卡'})
            except Exception as e:
                return JsonResponse({'code':1, 'info': '发生错误：' + str(e)})
        else:
            return JsonResponse({'code': 1, 'info': '提交数据缺失'})
    else:
        return JsonResponse({'code': 1, 'info': '请求方式错误'})
