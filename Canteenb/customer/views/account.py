# 2023-11-19
# 客户端账号相关
import json
import random
import uuid

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.core.cache import cache
from django.core.mail import send_mail
from django.http import JsonResponse
from django.middleware.csrf import get_token

from customer.models import Customer
import Canteen.settings as can_set
from lib.handler import request_handler


def get_csrf_token(request):
    return JsonResponse({'csrf_token': get_token(request)})


#  登录
def signin(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request=request, username=username, password=password)
        if user is not None:
            if user.is_active and user.usertype == 'customer':
                login(request, user)
                request.session['usertype'] = 'customer'
                return JsonResponse({'code': 0, 'info': '登录成功'})
            else:
                return JsonResponse({'code': 1, 'info': '该用户不符合权限或已禁用，请检查'})
        else:
            return JsonResponse({'code': 1, 'info': '账号或密码错误，请检查'})


# 登出
def signout(request):
    try:
        logout(request)
        # 清除session
        request.session.flush()
        return JsonResponse({'code': 0, 'info': '登出成功'})
    except Exception as e:
        return JsonResponse({'code': 1, 'info': '登出失败：' + str(e)})


# 新用户注册
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        fname = data.get('name')
        sex = data.get('sex', None)
        tel = data.get('tel', None)
        birth = data.get('birth', None)
        if username and password and email and fname:
            Customer.objects.create_user(username=username, password=password,
                                         email=email, is_superuser=0,
                                         first_name=fname, is_active=0,
                                         cus_sex=sex, cus_birth=birth,
                                         cus_tel=tel, usertype='customer')

            code = ''.join([str(random.randint(0, 9)) for _ in range(6)])
            cache.set(username, code, 1800)

            # 邮件激活
            sub = '【餐饮系统】用户激活邮件'
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
                    <p style="font-weight: lighter; font-size: 15px;">用 户 激 活 </p>
                    <p>尊敬的 {}<br>欢迎注册餐饮系统</p>
                    <div>
                        <p target="_blank">您的激活验证码为：<span style="font-weight: bolder; ">{}</span></p>
                    </div>
                    <br>
                </div>
            '''.format(fname, code)

            send_mail(subject=sub, message=msg, from_email=can_set.EMAIL_HOST_USER, recipient_list=[email, ],
                      html_message=msg)
            return JsonResponse({'code': 0, 'info': '注册提交成功'})
        else:
            return JsonResponse({'code': 1, 'info': '请填写完整信息'})
    else:
        return JsonResponse({'code': 1, 'info': '请使用POST方法调用此接口'})


# 激活账户
def active(request):
    data = json.loads(request.body)
    code = data.get('code')
    username = data.get('username')

    if cache.get(username) == code:
        user = Customer.objects.get(username=username)
        user.is_active = 1
        user.save()

        cache.delete(username)

        return JsonResponse({'code': 0, 'info': '激活成功'})
    else:
        return JsonResponse({'code': 1, 'info': '激活失败，验证码错误或用户不存在'})


# 使用邮件重置密码
def reset(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        try:
            user = Customer.objects.get(email=email)
        except Customer.DoesNotExist:
            return JsonResponse({'code': 1, 'info': f'用户不存在'})

        code = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        cache.set(email, code, 1800)

        fname = user.first_name

        # 密码重置邮件
        sub = '【餐饮系统】用户密码重置邮件'
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
                <p style="font-weight: lighter; font-size: 15px;">密 码 重 置 </p>
                <p>尊敬的 {}<br></p>
                <div>
                    <p target="_blank">您的重置验证码为：<span style="font-weight: bolder; ">{}</span></p>
                </div>
                <br>
            </div>
        '''.format(fname, code)
        send_mail(subject=sub, message=msg, from_email=can_set.EMAIL_HOST_USER, recipient_list=[email, ],
                  html_message=msg)
        return JsonResponse({'code': 0, 'info': '邮件发送成功'})
    else:
        return JsonResponse({'code': 1, 'info': '请使用POST方法调用此接口'})


# 重置密码
def reset_done(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        code = data.get('code')
        password = data.get('password')
        email = data.get('email')

        if cache.get(email) == code:
            user = Customer.objects.get(email=email)
            if user.usertype == 'customer':
                user.set_password(password)
                user.save()
                cache.delete(email)
                return JsonResponse({'code': 0, 'info': '密码重置成功'})
            else:
                return JsonResponse({'code': 1, 'info': '密码重置失败，用户类型校验失败'})
        else:
            return JsonResponse({'code': 1, 'info': '密码重置失败，用户不存在'})
    else:
        return JsonResponse({'code': 1, 'info': '禁止使用该方法提交数据'})
