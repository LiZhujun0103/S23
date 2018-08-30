import json, os
con1 = ['创建课程', '查看所有课程', '创建学生账号', '查看所有学生', '查看学生选课情况', '退出程序']
con2 = ['查看所有课程', '选择课程', '查看所选课程', '退出程序']
def pri(li):                                # 打印菜单函数，用于循环显示
    print('菜单'.center(50, '*'))
    for x, y in enumerate(li, 1):
        print(x, y)

def get_dic(filename):                      # 反序列化函数，用于读取序列化后存储的选课
    if os.path.exists(filename):
        with open(filename, mode='r', encoding='utf8') as f3:
            m_dic = json.load(f3)
    else:
        m_dic = {}
    return m_dic

ke_dic = get_dic('class_list')             # 加载可选课程

def chk_user(user):                        # 检查用户名是否存在的函数
    with open('user_info', mode='r', encoding='utf8') as file2:
        li = (i.strip('\n').split(':')[0] for i in file2)
        for x in li:
            if user == x:
                flag = 0
                break
        else:
            flag = 1
    return flag

def login(name, pasd):                     # 登陆函数，登陆成功和角色判定
    with open('user_info', mode='r', encoding='utf8') as file3:
        dic = {i.strip('\n').split(':')[0] : [i.strip('\n').split(':')[1], i.strip('\n').split(":")[2]] for i in file3}
        for k, v in dic.items():
            if k == name and v[0] == pasd:
                logind = 1
                loginr = v[1]
                break
        else:
            logind = 0
            loginr = '0'
    return [logind, loginr]

class kecheng:                                      # 定义课程类,课程需要名称，价格，老师，周期四个属性
    def __init__(self, name, price, tech, time):
        self.name = name
        self.price = price
        self.techer = tech
        self.time = time

class Stu:                                          # 定义学生类，创建一系列学生该有的方法
    def __init__(self, name):
        self.name = name
        self.pe_dic = get_dic(name)
    def ch_all_ke(self):                             # 查看所有可选课程
        print('所有可选课程如下：')
        for i in ke_dic.keys():
            print('课程【%s】,价格：%s,老师：%s,学习周期：%s' % (i, ke_dic[i][0], ke_dic[i][1], ke_dic[i][2]))
    def choice_ke(self):                            # 选择课程方法
        flag =1
        while flag:
            self.ch_all_ke()
            self.c_name = input('请输入要选择的课程名称：')
            lis = list(self.pe_dic.keys())
            for k, v in ke_dic.items():             # 判断课程是否存在
                if self.c_name == k and self.c_name not in lis:
                    self.pe_dic[self.c_name] = v
                    print('恭喜%s同学成功选择了%s课程，其价格为%s,任课老师为%s，上课周期为%s' % (self.name, self.c_name, v[0], v[1], v[2]))
                    cho = input('不再选课请输入q/Q，继续选课请输入其他任意键').strip().upper()
                    if cho == 'Q':
                        flag = 0
                        with open(self.name, mode='w', encoding='utf8') as w1:
                            json.dump(self.pe_dic, w1)
                        break
                    else:
                        break
            else:
                print('您选择的课程不存在或已经选择，请重新选择课程。')

    def lis_ke(self):
        if self.pe_dic:
            print('%s同学已经选择了如下课程：' % self.name)
            for k, v in self.pe_dic.items():
                print('课程【%s】,售价：%s,老师：%s,学习周期：%s' % (k, v[0], v[1], v[2]))
        else:
            print('%s同学还没有选择课程' % self.name)
class Adm(Stu):                                     # 创建管理员类，继承了学生类
    def __init__(self, name):
        self.name = name
    def course(self, kc_name, p, t, tm):            # 创建课程方法，课程有名称，价格，老师，周期四个参数需要传入
        kec_name = kecheng(kc_name, p, t, tm)
        ke_dic[kec_name.name] = [kec_name.price, kec_name.techer, kec_name.time]
        with open('class_list', mode='w', encoding='utf8') as f2:
            json.dump(ke_dic, f2)
        print('课程[%s]创建成功' % kec_name.name)
    def set_role(self):                             # 创建学生账户方法
        while 1:
            in_name = input('请输入新建的用户名：').strip()
            chk = chk_user(in_name)
            if chk == 1:
                in_pass = input('请输入密码：').strip()
                in_role = input('请输入角色(管理员输入a/学生输入s，时间紧迫未做验证，请不要输入其他字符)：').strip()
                with open('user_info', mode='a', encoding='utf8') as file1:
                    file1.write('%s:%s:%s\n' % (in_name, in_pass, in_role))
                print('用户%s添加成功' % in_name)
                break
            else:
                print('用户名已存在，请重新输入')
    def lookup(self):                               # 查看所有学生
        with open('user_info', mode='r', encoding='utf8') as f1:
            li = (i.strip('\n').split(':')[0] for i in f1)
            print('目前一共有如下学生：')
            for i in li:
                print(i)
    def ch_user_ke(self, user):                     # 查看学生选课情况，使用了组合学生类
        self.uname = Stu(user)
        self.uname.lis_ke()

print('欢迎登陆选课系统'.center(50, '-'))
count = 3
while count > 0:
    username = input('请输入用户名(管理员admin密码admin123，学生laohu密码12345)：').strip()
    userpass = input('请输入密码：').strip()
    a,b = login(username, userpass)
    if a == 0:
        count -= 1
        if count > 0:
            print('用户名或密码错误，还可输入%s次' % count)
        else:
            print('错误次数已达上限，拜拜')
    elif b == 'a':
        print('欢迎管理员%s' % username)
        ADMIN = Adm(username)
        while 1:
            pri(con1)
            ca = input('请选择您要进行的操作：').strip()
            if ca == '1':
                a1 = input('请输入课程名称：').strip()
                a2 = input('请输入课程价格：').strip()
                a3 = input('请输入授课老师：').strip()
                a4 = input('请输入课程周期：').strip()
                ADMIN.course(a1, a2, a3, a4)
            elif ca == '2':
                ADMIN.ch_all_ke()
            elif ca == '3':
                ADMIN.set_role()
            elif ca == '4':
                ADMIN.lookup()
            elif ca == '5':
                xname = input('请输入想要查看的学生姓名：').strip()
                if xname == ADMIN.name:
                    print('管理员不可选课')
                else:
                    ADMIN.ch_user_ke(xname)
            elif ca == '6':
                print('ByeBye %s' % username)
                exit(0)
            else:
                print('重新选择')
    elif b == 's':
        STU = Stu(username)
        print('欢迎%s同学' % username)
        while 1:
            pri(con2)
            sa = input('请选择您要进行的操作：').strip()
            if sa == '1':
                STU.ch_all_ke()
            elif sa == '2':
                STU.choice_ke()
            elif sa == '3':
                STU.lis_ke()
            elif sa == '4':
                print('ByeBye %s' % username)
                exit(0)
            else:
                print('重新选择')