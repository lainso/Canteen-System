import { createRouter, createWebHashHistory } from 'vue-router'

const router = createRouter({
  history: createWebHashHistory(import.meta.env.BASE_URL),
  routes: [
    // 开始定义客户路由
    {
      path: '/',
      redirect: '/login'
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/login.vue')
    },
    {
      path: '/index',
      name: 'index',
      component: () => import('../views/index.vue')
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('../views/register.vue')
    },
    {
      path: '/active',
      name: 'active',
      component: () => import('../views/active.vue')
    },
    {
      path: '/resetPass',
      name: 'resetPass',
      component: () => import('../views/resetPass.vue')
    },
    {
      path: '/resetDone',
      name: 'resetDone',
      component: () => import('../views/resetDone.vue')
    },
    {
      path: '/order',
      name: 'order',
      component: () => import('../views/order.vue')
    },
    {
      path: '/noti',
      name: 'noti',
      component: () => import('../views/noti.vue')
    },
    {
      path: '/cardApply',
      name: 'cardApply',
      component: () => import('../views/cardApply.vue')
    },
    {
      path: '/cardDel',
      name: 'cardDel',
      component: () => import('../views/cardDel.vue')
    },
    {
      path: '/cardUpdate',
      name: 'cardUpdate',
      component: () => import('../views/cardUpdate.vue')
    },
    {
      path: '/cardActive',
      name: 'cardActive',
      component: () => import('../views/cardActive.vue')
    },
    {
      path: '/me',
      name: 'me',
      component: () => import('../views/me.vue')
    },

    // 开始定义管理员路由
    {
      path: '/super',
      redirect: '/super/login'
    },
    {
      path: '/super/login',
      name: 'superLogin',
      component: () => import('../views/super/login.vue')
    },
    {
      path: '/super/index',
      name: 'superIndex',
      component: () => import('../views/super/index.vue')
    },
    {
      path: '/super/superAdmin',
      name: 'superAdmin',
      component: () => import('../views/super/superAdmin.vue')
    },
    {
      path: '/super/resetPass',
      name: 'superResetPass',
      component: () => import('../views/super/resetPass.vue')
    },
    {
      path: '/super/promo',
      name: 'superPromo',
      component: () => import('../views/super/promo.vue')
    },
    {
      path: '/super/customer',
      name: 'superCustomer',
      component: () => import('../views/super/customer.vue')
    },
    {
      path: '/super/shop',
      name: 'superShop',
      component: () => import('../views/super/shop.vue')
    },
    {
      path: '/super/me',
      name: 'superMe',
      component: () => import('../views/super/me.vue')
    },
    {
      path: '/super/emp',
      name: 'superEmp',
      component: () => import('../views/super/emp.vue')
    },
    {
      path: '/super/dish',
      name: 'superDish',
      component: () => import('../views/super/dish.vue')
    },
    {
      path: '/super/order',
      name: 'superOrder',
      component: () => import('../views/super/order.vue')
    },
    {
      path: '/super/payment',
      name: 'superPayment',
      component: () => import('../views/super/payment.vue')
    },
    {
      path: '/super/noti',
      name: 'superNoti',
      component: () => import('../views/super/noti.vue')
    },
    {
      path: '/super/paycard',
      name: 'superPaycard',
      component: () => import('../views/super/paycard.vue')
    },

    // 开始定义商户路由
    {
      path: '/joinShop',
      name: 'joinShop',
      component: () => import('../views/shop/joinShop.vue')
    },
    {
      path: '/shop',
      redirect: '/shop/login'
    },
    {
      path: '/shop/login',
      name: 'shopLogin',
      component: () => import('../views/shop/login.vue')
    },
    {
      path: '/shop/index',
      name: 'shopIndex',
      component: () => import('../views/shop/index.vue')
    },
    {
      path: '/shop/addOrder',
      name: 'shopAddOrder',
      component: () => import('../views/shop/addOrder.vue')
    },
    {
      path: '/shop/order',
      name: 'shopOrder',
      component: () => import('../views/shop/order.vue')
    },
    {
      path: '/shop/emp',
      name: 'shopEmp',
      component: () => import('../views/shop/emp.vue')
    },
    {
      path: '/shop/dish',
      name: 'shopDish',
      component: () => import('../views/shop/dish.vue')
    },
    {
      path: '/shop/me',
      name: 'shopMe',
      component: () => import('../views/shop/me.vue')
    },

    // 定义错误页
    {
      path: '/pageError',
      name: 'pageError',
      component: () => import('../components/pageError.vue')
    },
    {
      path: '/:catchAll(.*)',
      redirect: '/pageError'
    },
  ]
})

export default router 
