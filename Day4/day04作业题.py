from functools import wraps
import time
login_flag = 0                      # 定义变量判断是否登陆


def welcome_page():                                         # 欢迎页面函数
    context = '''1：请登陆
2：请注册
3：文章页面
4：日记页面
5：评论页面
6：收藏页面
7：注销
8：退出程序'''
    print('欢迎来到博客园首页'.center(40, '-'))
    print(context)

def getuser_info():                                     # 用户信息查询函数
    with open('register.txt', 'r', encoding='utf8') as file1:
        di1 = {i.rstrip('\n').split(':')[0] : i.rstrip('\n').split(':')[1] for i in file1}
        return di1

def login():                                        # 登陆函数,三次登陆失败退出
    global login_flag, users
    user_dic = getuser_info()
    count = 0
    while count < 3:
        users = input('请输入用户名：').strip()
        paswd = input('请输入密码：').strip()
        for k, v in user_dic.items():
            if users == k and paswd == v:
                count = 3
                login_flag = 1
                break
        else:
            count += 1
            if count < 3:
                print('用户名不存在或密码错误，请重新输入')
            else:
                print('错误次数已达上限，拜拜')
                exit(0)

def zhuce():                                    # 注册函数
    global login_flag, users
    dic = getuser_info()
    while 1:
        users = input('请输入用户名：').strip()
        pawd = input('请输入密码：').strip()
        li1 = [k for k in dic]
        if users in li1:
            print('用户名已存在，请重新输入')
            continue
        else:
            with open('register.txt', mode='a', encoding='utf8') as file2:
                file2.write('%s:%s\n' % (users, pawd))
                login_flag = 1
                print('用户%s注册成功，并已自动登陆...' % users)
                break

def lo_gs(x):                                           # 访问成功后的记录函数
    with open('logs.txt', mode='a', encoding='utf8') as file3:
        struct_time = time.localtime()
        tm = time.strftime("%Y-%m-%d %H:%M:%S", struct_time)
        fn = x.__name__
        file3.write('用户:%s在%s执行了%s函数\n' % (users, tm, fn))

def zhuxiao():                                      # 注销函数
    global login_flag
    if login_flag == 0:
        print('您没有登陆，无需注销')
    else:
        login_flag = 0
        print('用户%s已注销登陆' % users)

def check(funs):                                        # 装饰器函数,访问页面前判断是否登陆
    @wraps(funs)
    def inn():
        if login_flag == 1:
            lo_gs(funs)
            res = funs()
            return res
        else:
            cho = input('您没有登陆，登陆请输入1，注册请输入2：').strip()
            if cho == '1':
                login()
                lo_gs(funs)
                res = funs()
                return  res
            elif cho == '2':
                zhuce()
                lo_gs(funs)
                res = funs()
                return res
            else:
                print('您输入错误，请重新开始程序')
                exit(0)
    return inn


@check
def wenzhang():
    print('---------------欢迎%s访问评论文章页面---------------' % users)

@check
def riji():
    print('---------------欢迎%s访问评论日志页面---------------' % users)

@check
def pinglun():
    print('---------------欢迎%s访问评论页面-------------------' % users)

@check
def shoucang():
    print('---------------欢迎%s访问收藏页面--------------------' % users)


while 1:                                    # 主执行函数
    welcome_page()
    you_choice = input('请输入您选择的编码：').strip()
    if you_choice.isdigit() and 1 <= int(you_choice) <= 8 :
        if you_choice == '1':
            if login_flag == 1:
                print('亲爱的%s您已经登陆，请继续访问。' % users)
            else:
                login()
        elif you_choice == '2':
            if login_flag == 1:
                print('亲爱的%s您已经登陆，请继续访问。' % users)
            else:
                zhuce()
        elif you_choice == '3':
            wenzhang()
        elif you_choice == '4':
            riji()
        elif you_choice == '5':
            pinglun()
        elif you_choice == '6':
            shoucang()
        elif you_choice == '7':
            zhuxiao()
        else:
            print('谢谢访问，再见！')
            exit(0)
    else:
        print('您输入有误，请重新选择')