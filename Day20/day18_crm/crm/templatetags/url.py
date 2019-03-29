from django import template
from django.urls import reverse
register = template.Library()


@register.simple_tag()
def reverse_url(request, name, *args, **kwargs):
    """
    :param request:
    :param name:
    :param args:
    :param kwargs:
    :return:
    """

    base_url = reverse(name, args=args, kwargs=kwargs)

    param = request.GET.urlencode()

    url = "{}?{}".format(base_url, param)

    return url
