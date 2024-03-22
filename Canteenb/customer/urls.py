from django.urls import path

from customer.views import account, order, paycard, customer, notice, promo

urlpatterns = [
    path('order', order.query_orders),
    path('paycard', paycard.handler),
    path('customer', customer.handler),
    path('notice', notice.query),
    path('promo', promo.verify),

    path('account/signin', account.signin),
    path('account/register', account.register),
    path('account/active', account.active),
    path('account/resetPass', account.reset),
    path('account/resetDone', account.reset_done),
    path('account/signout', account.signout),
]
