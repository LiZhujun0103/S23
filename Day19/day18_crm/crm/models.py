from django.db import models
from rbac.models import UserInfo as RbacUserInfo

# Create your models here.
class Department(models.Model):
    """
    部门表
    """
    title = models.CharField(max_length=32, verbose_name='部门名称')

    def __str__(self):
        return self.title

    # class Meta:
    #     db_table='xxxx'


class Maintions(models.Model):
    # 主机表
    mid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, verbose_name='主机名')


# class UserInfo(models.Model):
#     name = models.CharField(max_length=32, verbose_name='用户名')
#     password = models.CharField(max_length=32, verbose_name='密码')
#     depart = models.ForeignKey(to='Department',on_delete=models.CASCADE, verbose_name='部门名称')


class UserInfo(RbacUserInfo):
    # name = models.CharField(max_length=32, verbose_name='用户名')
    # password = models.CharField(max_length=32, verbose_name='密码')
    # gener_choice = ((0, '男'), (1, '女'))
    # gener = models.IntegerField(choices=gener_choice)
    depart = models.ForeignKey(to='Department', on_delete=models.CASCADE, verbose_name='部门名称')

    def __str__(self):
        return self.name
