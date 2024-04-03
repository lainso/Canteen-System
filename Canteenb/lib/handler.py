# 2023-11-14
import json
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
import Canteen.settings as can_set


def request_handler(request, options):
    # 无用户类型session处理
    if 'usertype' not in request.session:
        return JsonResponse({
            'code': 302,
            'info': '未登录，请检查',
            'redirect': '/#/pageError'},
            status=302
        )

    # 用户类型非法session处理
    if request.session['usertype'] not in ['super', 'customer', 'shop']:
        return JsonResponse({
            'code': 302,
            'info': '未登录，请检查',
            'redirect': '/#/pageError'},
            status=302
        )

    # 获取参数
    if request.method == 'GET':
        request.params = request.GET
    elif request.method in ['POST', 'PUT', 'DELETE']:
        request.params = json.loads(request.body)

    action = request.params['action']

    if action in options:
        function = options[action]
        return function(request)
    else:
        # 请求方法错误处理
        return JsonResponse({
            'code': 302,
            'info': '发生错误，请重新登录',
            'redirect': '/#/pageError'},
            status=302
        )
