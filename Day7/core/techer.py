from lib import getinfo
from conf import settings
from core import student_class, kecheng, login


class Tech(student_class.Stu):
    operate_lis = [('查看所有课程', 'all_ke'), ('查看所教班级', 'chk_ban'), ('查看班级中的学生', 'chk_ban_stu'), ('退出', 'exi')]

    def __init__(self, name):
        self.name = name
        self.cls_name = getinfo.get_class(settings.user_info, self.name)

    def chk_ban(self):
        print('%s讲师当前所教班级为：%s' % (self.name, self.cls_name))

    def chk_ban_stu(self):
        clas = getinfo.get_info(settings.bjfile)
        stu_lis = clas[self.cls_name][1]
        print('班级%s中有如下学生:' % self.cls_name)
        for i in stu_lis:
            print(i)

    def exi(self):
        exit('再见%s老师' % self.name)
