from django import template

register = template.Library()


from django.conf import settings
import re


@register.filter
def add_sd(value, arg):
    return "{}-{}".format(value, arg)


@register.simple_tag
def join(*args, **kwargs):
    return "{}-{}".format('-'.join(args), '*'.join(kwargs.values()))


@register.inclusion_tag('menu.html')
def menu(request):
    url = request.path_info
    menu_list = request.session.get(settings.MENU_SESSION_KEY)
    for i in menu_list:
        if re.match(i['url'],url):
            i['class'] = 'active'
    return {'menu_list': menu_list}


@register.filter()
def has_permission(request, name):
    permission_dict = request.session.get(settings.PERMISSION_SESSION_KEY)
    if name in permission_dict:
        return True
