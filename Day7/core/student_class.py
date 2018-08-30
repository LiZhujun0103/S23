from lib import getinfo
from conf import settings

class Stu:
    operate_lis = [('查看可选课程', 'all_ke'), ('选择课程', 'choice_ke'), ('查看已选课程', 'show_ke'), ('退出', 'exi')]

    def __init__(self, name):
        self.name = name
        self.dic = getinfo.get_info(settings.stu_class)
        self.ke = getinfo.get_info(settings.stu_class).get(name)
        if not self.ke:
            self.ke = []
        self.allk = getinfo.get_info(settings.class_list)

    def all_ke(self):
        all = getinfo.get_info(settings.class_list)
        print('所有可选课程如下：')
        for i in all.keys():
            print('课程【%s】，价格：%s，授课老师：%s，学习时长：%s' % (i, all[i][0], all[i][1], all[i][2]))

    def choice_ke(self):
        flag = 1
        while flag:
            self.all_ke()
            self.c_name = input('请输入要选择的课程名称:').strip()
            for k, v in self.allk.items():
                if self.c_name == k and self.c_name not in self.ke:
                    self.ke.append(k)
                    print('恭喜%s同学成功选择了%s课程' % (self.name, self.c_name))
                    cho = input('退出选课请按q/Q，继续选课请按其他任意键...').strip().upper()
                    if cho == 'Q':
                        flag = 0
                        self.dic[self.name] = self.ke
                        getinfo.set_info(self.dic, settings.stu_class)
                        break
                    else:
                        break
            else:
                print('您选择的课程不存在或者已经选择完成，请重新选择课程。')

    def show_ke(self):
        if self.ke:
            print('%s同学已经选择了如下课程：' % self.name)
            for i in self.ke:
                print(i)
        else:
            print('%s同学还没有选择任何课程。' % self.name)

    def exi(self):
        exit('再见，%s同学' % self.name)