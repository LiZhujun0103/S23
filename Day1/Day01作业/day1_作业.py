# -*- coding:utf-8 -*-
# Author: ZhuJun.li

# 定义账户密码及尝试登陆次数
username = 'eric.zj.l'
password = 'GoodBoy'
count = 4

while count > 0:
    in_name = input('请输入用户名：')
    in_pass = input('请输入密码：')
    if in_name == username and in_pass == password:     # 判断输入的用户名和密码是否正确
        print('登陆成功')
        break
    else:
        count -= 1
        if count != 0:
            print('用户名或密码错误，还可重试 %d 次' % count)
        else:
            print('输入错误次数已达上限，ByeBye！')
