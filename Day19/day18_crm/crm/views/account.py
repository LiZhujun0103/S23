from django.shortcuts import render, HttpResponse, redirect, reverse
from crm import models
from django.conf import settings


def login(request):
    err_msg = ''
    if request.method == 'POST':
        user = request.POST.get('username')
        pwd = request.POST.get('password')
        obj = models.UserInfo.objects.filter(name=user, password=pwd).first()
        if not obj:
            err_msg = '用户名或密码错误'
        else:
            # 登录成功
            # 记录权限的信息
            # 查询权限信息： isnull=False  跨表  去重
            permission_list = obj.roles.all().filter(permissions__url__isnull=False).values(
                                   'permissions__url',
                                   'permissions__title',
                                   'permissions__name',
                                   'permissions__is_menu',
                                   ).distinct()
            # 构建数据结构
            # 权限的字典
            permission_dict = {}
            # 菜单的列表
            menu_list = []
            for i in permission_list:
                if i['permissions__is_menu']:
                    menu_list.append({
                        'url':i['permissions__url'],
                        'title':i['permissions__title']
                    })
                permission_dict[i['permissions__name']] = {'url': i['permissions__url']}

            # 存入session
            request.session[settings.PERMISSION_SESSION_KEY]=permission_dict
            request.session[settings.MENU_SESSION_KEY]=menu_list

            return redirect(reverse('index'))

    return render(request, 'login.html', {'err_msg': err_msg})
