# customer\models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# 顾客信息
class Customer(AbstractUser):
    # 客户电话
    cus_tel = models.CharField(max_length=15)
    cus_sex = models.CharField(max_length=10, blank=True, null=True)
    cus_birth = models.CharField(max_length=25, blank=True, null=True)
    # 收货地址
    cus_address = models.TextField(blank=True, null=True)
    usertype = models.CharField(max_length=10, default='customer')

# 支付卡信息
class Paycard(models.Model):
    # 支付卡卡号
    card_number = models.CharField(max_length=16)
    # 支付卡余额
    card_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # 支付卡状态:未激活，已激活，已冻结，已注销
    card_condition = models.CharField(max_length=20, default='未激活')
    # 支付卡拥有者，关联顾客id
    cus_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
