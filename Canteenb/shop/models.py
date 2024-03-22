# shop\models.py
from django.db import models
from customer.models import Customer


# Create your models here.
# 员工信息
class Employee(models.Model):
    emp_name = models.CharField(max_length=20)
    # 员工编号
    emp_number = models.CharField(max_length=20)
    # 员工电话
    emp_tel = models.CharField(max_length=20)
    # 员工状态
    emp_condition = models.CharField(max_length=20)
    # 员工角色如普通员工、店长
    emp_role = models.CharField(max_length=50, default='普通员工')
    # 员工所属店铺，关联shop的id
    emp_shop = models.ForeignKey('Shop', on_delete=models.CASCADE)


# 门店信息
class Shop(models.Model):
    # 名字
    shop_name = models.CharField(max_length=100)
    # 门店编号
    shop_number = models.CharField(max_length=20, unique=True)
    # 门店电话
    shop_tel = models.CharField(max_length=20)
    # 门店负责人
    shop_head = models.CharField(max_length=50)
    # 门店口令，用于员工注册时填写并加入
    shop_pass = models.CharField(max_length=50)
    shop_cus = models.ForeignKey(Customer, on_delete=models.CASCADE)


# 餐品信息
class Dish(models.Model):
    dish_name = models.CharField(max_length=100)
    # 菜品描述
    dish_des = models.TextField(blank=True, null=True)
    dish_price = models.DecimalField(max_digits=10, decimal_places=2)
    # 菜品图片url
    dish_img = models.URLField(blank=True, null=True)
    # 菜品所属店铺
    dish_shop = models.ForeignKey(Shop, on_delete=models.PROTECT)


# 订单信息
class Order(models.Model):
    # 订单号，需要生成唯一订单号
    ord_number = models.CharField(max_length=20, unique=True)
    ord_time = models.CharField(max_length=50)
    # 哪位顾客的订单
    cus_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # 顾客在哪个店买的菜
    ord_shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    # 订单状态
    ord_condition = models.CharField(max_length=50, default='默认状态')
    # 订单金额
    ord_money = models.DecimalField(max_digits=10, decimal_places=2, default=0)


# 订单与菜品关系
class OrderList(models.Model):
    # 订单号,关联订单信息
    ord_number = models.ForeignKey(Order, on_delete=models.CASCADE, to_field='ord_number')
    # 菜品id
    dish = models.ForeignKey(Dish, on_delete=models.SET_NULL, null=True, blank=True)
    # 选购数量
    ordlist_num = models.PositiveIntegerField()
