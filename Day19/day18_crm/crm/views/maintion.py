from django.shortcuts import render, redirect, reverse
from crm import models
from crm.utils.pager import Pagination
from crm.forms.my_form import MainModelForm


def server_list(request):
    page = request.GET.get('page')  # 获取访问的分页页码
    count = models.Maintions.objects.all().count()  # 获取总条数
    pager = Pagination(page, count, request.path_info)

    all_depart = models.Maintions.objects.all()[pager.start:pager.end]  # 切片页面
    return render(request, 'server_list.html',
                  {'all_depart': all_depart, 'page_html': pager.page_html})


def servers(request, edit_sid=None):
    edit_obj = models.Maintions.objects.filter(mid=edit_sid).first()
    form_obj = MainModelForm(instance=edit_obj)
    if request.method == 'POST':
        form_obj = MainModelForm(data=request.POST, instance=edit_obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse('server_list'))
    return render(request, 'change.html', {'form_obj': form_obj})


def server_del(request, del_id):
    models.Maintions.objects.filter(mid=del_id).delete()
    return redirect(reverse('server_list'))