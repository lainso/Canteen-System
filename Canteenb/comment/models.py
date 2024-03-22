# comment\models.py
from django.db import models
from customer.models import Customer
from shop.models import Shop, Order

# Create your models here.
# 通知信息
class Notifications(models.Model):
    noti_title = models.CharField(max_length=50)
    noti_content = models.TextField()
    # 发送时间
    noti_sendtime = models.CharField(max_length=25)
    # 发送对象，目标为客户id
    cus_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

# 促销活动信息
class Promotions(models.Model):
    promo_name = models.CharField(max_length=100)
    promo_code = models.CharField(max_length=20,unique=True, default=None)
    promo_multiple = models.DecimalField(max_digits=10, decimal_places=2, default=1)
    # 促销开始日期
    promo_start = models.CharField(max_length=25)
    # 促销结束日期
    promo_end = models.CharField(max_length=25)

# 交易信息
class Payment(models.Model):
    # 支付订单号
    pay_num = models.CharField(max_length=25)
    pay_time = models.CharField(max_length=25)
    # 支付金额，需与订单金额比对
    pay_money = models.DecimalField(max_digits=10, decimal_places=2)
    # 支付方式
    pay_way = models.CharField(max_length=50)
    # 关联订单
    ord_id = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
