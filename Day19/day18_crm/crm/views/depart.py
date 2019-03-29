from django.shortcuts import render, redirect, reverse
from crm import models
from crm.utils.pager import Pagination
from crm.forms.my_form import DepartModelForm


# def depart_list(request):
#     # 获取所有的数据
#     all_depart = models.Department.objects.all()
#     return render(request, 'depart_list.html', {'all_depart': all_depart})


def depart_list(request):
    page = request.GET.get('page')  # 获取访问的分页页码
    count = models.Department.objects.all().count()  # 获取总条数
    pager = Pagination(page, count, request.path_info)

    all_depart = models.Department.objects.all()[pager.start:pager.end]  # 切片页面
    return render(request, 'depart_list.html',
                  {'all_depart': all_depart, 'page_html': pager.page_html})


# class DepartModelForm(forms.ModelForm):
#     class Meta:
#         model = models.Department
#         fields = '__all__'
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "部门名称"})
#         }
#         error_messages = {
#             'title': {
#                 'required': '不能为空'
#             }
#         }


def depart_add(request):
    form_obj = DepartModelForm()
    if request.method == 'POST':
        form_obj = DepartModelForm(data=request.POST)
        if form_obj.is_valid():  # 对数据进行校验
            # 保存数据
            # models.Department.objects.create(**form_obj.cleaned_data)
            form_obj.save()
            return redirect(reverse('depart_list'))
    return render(request, 'depart_form.html', {'form_obj': form_obj})


def depart_edit(request, edit_id):
    edit_obj = models.Department.objects.filter(id=edit_id).first()
    form_obj = DepartModelForm(instance=edit_obj)
    if request.method == 'POST':
        form_obj = DepartModelForm(data=request.POST, instance=edit_obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse('depart_list'))
    return render(request, 'depart_form.html', {'form_obj': form_obj})


def depart_del(request, del_id):
    # print(del_id)
    models.Department.objects.filter(id=del_id).delete()
    return redirect(reverse('depart_list'))
