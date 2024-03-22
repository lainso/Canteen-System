# 2023-12-09
# 客户端：优惠码验证
from django.http import JsonResponse
from comment.models import Promotions


def verify(request):
    if request.method == 'POST':
        promo_code = request.GET.get('promo_code')
        try:
            promo = Promotions.objects.get(promo_code=promo_code)
            if promo:
                return JsonResponse({'code': 0, 'info': '促销活动验证成功', 'multi': promo.promo_multiple})
            else:
                return JsonResponse({'code': 1, 'info': '促销活动验证失败'})
        except Exception as e:
            return JsonResponse({'code': 2, 'info': '促销活动验证失败：' + str(e)})
    else:
        return JsonResponse({'code': 1, 'info': '禁止使用该方法提交数据'})
