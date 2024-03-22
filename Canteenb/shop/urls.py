from django.urls import path

from shop.views import employee, shop, dish, order, account, payment, paycard

urlpatterns = [
    path('employee', employee.handler),
    path('shop', shop.handler),
    path('dish', dish.handler),
    path('order', order.handler),
    path('payment', payment.add),
    path('paycard', paycard.update),
    path('joinShop', employee.join_by_code),

    path('account/signin', account.signin),
    path('account/signout', account.signout),
    path('account/reset', account.reset),
]

