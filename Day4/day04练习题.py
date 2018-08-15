from functools import wraps
import time
# 1.整理装饰器的形成过程，背诵装饰器的固定格式
# 装饰器是将一个函数镶嵌在另一个函数中进行重复使用的目的，增加函数的功能
def wra(fun):
    def inner(*args, **kwargs):
        print('before'.center(30, '-'))
        res = fun(*args, **kwargs)
        print('after'.center(30, '-'))
        return res
    return inner

@wra
def a1(a):
    print('wo shi %s' % a)
    return 'a1'

print(a1('xxx'))

# # 2.编写装饰器,在每次执行被装饰函数之前打印一句’每次执行被装饰函数之前都得先经过这里,这里根据需求添加代码'
def wra1(fun1):
    def inn1(*args, **kwargs):
        print('每次执行被装饰函数之前都得先经过这里，这里根据需求添加代码')
        res1 = fun1(*args, **kwargs)
        return res1
    return inn1
@wra1
def a2():
    print('我是被装饰函数')

a2()

# # 3. 编写装饰器,在每次执行被装饰函数之后打印一句’每次执行完被装饰函数之后都得先经过这里,这里根据需求添加代码
def wra2(fun2):
    def inn2(*args, **kwargs):
        res2 = fun2(*args, **kwargs)
        print('每次执行完被装饰函数之后都得先经过这里,这里根据需求添加代码')
        return res2
    return inn2

@wra2
def a3():
    print('我是被装饰函数')

a3()

# # 4.编写装饰器,在每次执行被装饰函数之前让用户输入用户名,密码,给用户三次机会,登录成功之后,才能访问该函数
def wra3(fun3):
    def inn3(*args, **kwargs):
        user = 'eric'
        pasd = 'ace123'
        c = 0
        while c < 3:
            user_name = input('请输入用户名：').strip()
            user_pass = input('请输入密码：').strip()
            if user_name == user and user_pass == pasd:
                res4 = fun3()
                return res4
            else:
                print('账号或密码错误，请重新输入')
                c += 1
                if c >= 3:
                    print('错误次数已达上限，拜拜')
                    break
    return inn3

@wra3
def a4():
    print('我是a4')
    return "x"

a4()

# 5.编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件,只支持单用户的账号密码,给用户三次机会），要求登录成功一次，
# 后续的函数都无需再输入用户名和密码
loged = 0
def getuser():
    with open('user_info.txt', 'r', encoding='utf8') as file2:
        di1 = {i.rstrip('\n').split(':')[0] : i.rstrip('\n').split(':')[1] for i in file2}
        return di1


def login1(fun4):
    def inn4(*args, **kwargs):
        global loged
        if loged == 0:
            count = 0
            while count < 3:
                uinfo = getuser()
                users = input('请输入用户名：').strip()
                paswd = input('请输入密码：').strip()
                for k, v in uinfo.items():
                    if users == k and paswd == v:
                        loged = 1
                        rrr = fun4(*args, **kwargs)
                        return rrr
                else:
                    print('用户名或密码错误')
                    count += 1
        else:
            rrr = fun4(*args, **kwargs)
            return rrr
    return inn4


@login1
def aa1(s):
    print('你输入了一个%s' % s)
    return 'frst'

@login1
def aa2():
    print('第二部')
    return 'second'


eri = aa1("d")
vv = aa2()
print(eri)
print(vv)

# 6.编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件,可支持多账号密码），要求登录成功一次（给三次机会），
# 后续的函数都无需再输入用户名和密码
# 见第五题代码，支持多账号

# 7.给每个函数写一个记录日志的功能
def wr(fun5):
    @wraps(fun5)
    def inn5(*args, **kwargs):
        with open('log.txt', mode='a+', encoding='utf8') as file3:
            struct_time = time.localtime()
            tm = time.strftime("%Y-%m-%d %H:%M:%S", struct_time)
            fn = inn5.__name__
            file3.write('%s  %s\n' % (fn, tm))
            ress = fun5(*args, **kwargs)
            return ress
    return inn5

@wr
def test_a(a, b):
    print("this %s, and %s" % (a, b))


test_a("xcv", "bnm")