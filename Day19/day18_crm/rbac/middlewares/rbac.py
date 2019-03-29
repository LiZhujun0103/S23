from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse
import re
from django.conf import settings


class RbacMiddleware(MiddlewareMixin):
    def process_request(self, request):
        url = request.path_info
        # 白名单校验
        # valid_list = [
        #     '/crm/login/',
        #     '/admin.*',
        # ]
        for i in settings.RBAC_VALID_LIST:
            if re.match(i,url):
                return
        # 权限的校验
        # 获取当前用户的权限信息
        permission_dict = request.session.get(settings.PERMISSION_SESSION_KEY)
        if not permission_dict:
            return HttpResponse('没有权限信息，请登录')
        # 进行权限信息的校验
        for k,v in permission_dict.items():
            reg_url = "{}$".format(v['url'])
            if re.match(reg_url,url):
                return
        # 登录后不需要权限的地址
        for i in settings.RBAC_NO_PERMISSION_LIST:
            if re.match(i,url):
                return

        return HttpResponse('没有相关的权限')

