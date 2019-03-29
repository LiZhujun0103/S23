from django.shortcuts import render, redirect, reverse
from crm import models
from crm.forms.my_form import UserModelForm


# dep = models.Department.objects.all()


# class UserModelForm(forms.ModelForm):
#     class Meta:
#         model = models.UserInfo
#         fields = '__all__'
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "用户名"}),
#             'password': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "密码"}),
#             'depart': forms.Select(attrs={'class': 'form-control'})
#         }
#         error_messages = {
#             'name': {
#                 'required': '不能为空'
#             },
#             'password': {
#                 'required': '需要设置密码'
#             }
#         }


def user_list(request):
    all_user = models.UserInfo.objects.all()
    return render(request, 'user_list.html', {'all_user': all_user})


def user_add(request):
    form_obj = UserModelForm()
    if request.method == 'POST':
        form_obj = UserModelForm(data=request.POST)
        if form_obj.is_valid():  # 对数据进行校验
            # 保存数据
            # models.Department.objects.create(**form_obj.cleaned_data)
            form_obj.save()
            return redirect(reverse('user_list'))
    return render(request, 'change.html', {'form_obj': form_obj})


def user_edit(request, edit_id):
    edit_obj = models.UserInfo.objects.filter(id=edit_id).first()
    form_obj = UserModelForm(instance=edit_obj)
    if request.method == 'POST':
        form_obj = UserModelForm(data=request.POST, instance=edit_obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse('user_list'))
    return render(request, 'change.html', {'form_obj': form_obj})


def users(request, edit_id=None):
    edit_obj = models.UserInfo.objects.filter(id=edit_id).first()
    form_obj = UserModelForm(instance=edit_obj)
    if request.method == 'POST':
        form_obj = UserModelForm(data=request.POST, instance=edit_obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse('user_list'))
    return render(request, 'change.html', {'form_obj': form_obj})


def user_del(request, del_id):
    models.UserInfo.objects.filter(id=del_id).delete()
    return redirect(reverse('user_list'))
