# 2023-12-03
# 管理员端：登入登出
import json

from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse

from customer.models import Customer
import Canteen.settings as set


#  登录
def signin(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    user = authenticate(request=request, username=username, password=password)
    if user is not None:
        if user.is_active and user.usertype == 'super':
            login(request, user)
            request.session['usertype'] = 'super'
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
        return JsonResponse({'code': 1, 'info': '登出失败' + str(e)})

# 重置密码
def reset(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        old_pass = data.get('old_pass')
        new_pass = data.get('new_pass')
        if username and old_pass and new_pass:
            try:
                user = authenticate(request=request, username=username, password=old_pass)
                if user is not None and user.usertype=='super':
                    user.set_password(new_pass)
                    user.save()
                    return JsonResponse({'code': 0, 'info': '重置成功'})
                else:
                    return JsonResponse({'code': 1, 'info': '旧密码输入错误，请检查'})
            except Exception as e:
                return JsonResponse({'code': 1, 'info': '重置密码失败：' + str(e)})
        else:
            return JsonResponse({'code': 1, 'info': '缺少必要数据'})
    else:
        return JsonResponse({'code': 1, 'info': '禁止使用该方法提交'})

def resetDef(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        if username:
            try:
                user = Customer.objects.get(username=username)
                if user is not None and user.usertype=='super':
                    user.set_password(set.ADMIN_DEFAULT_PASS)
                    user.save()
                    return JsonResponse({'code': 0, 'info': '重置成功'})
                else:
                    return JsonResponse({'code': 1, 'info': '未找到合法用户，请检查'})
            except Exception as e:
                return JsonResponse({'code': 1, 'info': '重置密码失败：' + str(e)})
        else:
            return JsonResponse({'code': 1, 'info': '缺少必要数据'})
    else:
        return JsonResponse({'code': 1, 'info': '禁止使用该方法提交'})
