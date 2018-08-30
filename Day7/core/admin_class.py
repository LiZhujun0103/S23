import hashlib
from lib import getinfo
from conf import settings
from core import student_class, kecheng, login, ban
md5 = hashlib.md5()

class Adm(student_class.Stu):
    operate_lis = [('创建课程', 'create_ke'), ('创建学生账号', 'create_role'), ('查看所有课程', 'all_ke'),
                   ('查看所有学生', 'check_all_stu'), ('查看所有学生选课情况', 'show_user_ke'), ('创建讲师', 'create_role'),
                   ('为讲师指定班级', 'tech_ban'), ('创建班级', 'create_ban'), ('为学生指定班级', 'stu_ban'),
                   ('退出程序', 'exi')]
    def __init__(self, name):
        self.name = name
        self.dic = getinfo.get_info(settings.class_list)
        self.ban_dic = getinfo.get_info(settings.bjfile)

    def create_ke(self):
        kname = input('课程名：')
        kprice = input('课程价格：')
        ktech = input('授课讲师：')
        ktimi = input('学习周期：')
        if not self.dic.get(kname):
            kc = kecheng.Course(kname, kprice, ktech, ktimi)
            self.dic[kc.name] = [kc.price, kc.tech, kc.timi]
            getinfo.set_info(self.dic, settings.class_list)
            print('课程【%s】创建成功' % kc.name)
        else:
            print('课程已经存在！')

    def create_role(self):
        while 1:
            in_name = input('请输入要创建的用户名称：').strip()
            chk = login.Login.chk_user(in_name)
            if chk == 1:
                in_pass = input('请输入密码：').strip()
                md5.update(in_pass.encode('utf8'))
                in_pass = md5.hexdigest()
                in_role = input('请输入角色类型（管理员：adm,学生：stu,讲师：tec）:').strip()
                in_ban = input('请指定班级，默认没有班级').strip()
                if not in_ban:
                    in_ban = ''
                getinfo.create_user(settings.user_info, in_name, in_pass, in_role, in_ban)
                print('用户%s添加成功' % in_name)
                break
            else:
                print('用户已存在，请重新输入')

    def check_all_stu(self):
        self.all_stu = getinfo.get_all_stu(settings.user_info)
        print('当前已创建的学生如下：')
        for i in self.all_stu:
            print(i)

    def show_user_ke(self):
        self.userke = getinfo.get_info(settings.stu_class)
        for k, v in self.userke.items():
            print('%s同学已选的课有%s' % (k, v))

    def create_ban(self):
        self.bname = input('请输入班级名称：').strip()
        bj = ban.Ban(self.bname)
        self.ban_dic.setdefault(bj.name, [bj.ban_tec, bj.ban_stu])
        getinfo.set_info(self.ban_dic, settings.bjfile)
        print('班级%s创建成功' % bj.name)

    def tech_ban(self):
        while 1:
            in_name = input('请输入讲师名称：').strip()
            chk = login.Login.chk_user(in_name)
            if chk == 0:
                in_ban = input('请指定班级').strip()
                if not in_ban:
                    print('不可输入空，请重新输入')
                    break
                getinfo.set_bj(settings.user_info, in_name, in_ban)
                self.ban_dic[in_ban][0].append(in_name)
                getinfo.set_info(self.ban_dic, settings.bjfile)
                print('讲师%s班级指定成功' % in_name)
                break
            else:
                print('讲师不存在，请重新输入')

    def stu_ban(self):
        while 1:
            in_name = input('请输入学生名称：').strip()
            chk = login.Login.chk_user(in_name)
            if chk == 0:
                in_ban = input('请指定班级').strip()
                if not in_ban:
                    print('不可输入空，请重新输入')
                    break
                getinfo.set_bj(settings.user_info, in_name, in_ban)
                self.ban_dic[in_ban][1].append(in_name)
                getinfo.set_info(self.ban_dic, settings.bjfile)
                print('学生%s班级指定成功' % in_name)
                break
            else:
                print('学生不存在，请重新输入')

    def exi(self):
        exit('再见%s' % self.name)