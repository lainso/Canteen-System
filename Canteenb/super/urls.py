from django.urls import path

from super.views import account, notice, promo, customer, payment, paycard, employee, dish, order, shop

urlpatterns = [
    path('notice',notice.handler),
    path('promo',promo.handler),
    path('customer', customer.handler),
    path('payment', payment.handler),
    path('paycard', paycard.handler),
    path('employee', employee.handler),
    path('dish', dish.handler),
    path('order', order.handler),
    path('shop', shop.handler),

    path('account/signin', account.signin),
    path('account/signout', account.signout),
    path('account/reset', account.reset),
    path('account/resetDef', account.resetDef),
]
