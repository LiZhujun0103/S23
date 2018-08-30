from core import login, admin_class, kecheng, student_class, techer

def show():
    print('欢迎登陆选课系统'.center(50, '-'))
    count = 3
    while count > 0:
        username = input('请输入用户名(管理员admin，密码admin123,讲师lzh，密码abc123,学生sjt，密码123)：').strip()
        userpawd = input('请输入密码(运行前请先阅读readme文件)：').strip()
        a , b = login.Login.lgn_ok(username,userpawd)
        if a == 0:
            count -= 1
            if count > 0:
                print('用户名或密码错误，还可以输入%s次' % count)
            else:
                print('错误次数已达上限，拜拜。')
        elif b == 'adm':
            print('欢迎管理员%s上线' % username)
            ADMIN = admin_class.Adm(username)
            while 1:
                for index, x in enumerate(ADMIN.operate_lis, 1):
                    print(index,x[0])
                ch = input('请选择您要进行的操作编号：').strip()
                if ch.isdigit() and 0 < int(ch) < 11:
                    ch = int(ch)
                    getattr(ADMIN, ADMIN.operate_lis[ch-1][1])()
                else:
                    print('重新选择')
        elif b == 'stu':
            print('欢迎%s同学上线' % username)
            STU = student_class.Stu(username)
            while 1:
                for index, x in enumerate(STU.operate_lis, 1):
                    print(index, x[0])
                ch = input('请选择要进行的操作编号：').strip()
                if ch.isdigit() and 0 < int(ch) < 5:
                    ch = int(ch)
                    getattr(STU, STU.operate_lis[ch-1][1])()
                else:
                    print('重新选择')
        elif b == 'tec':
            print('欢迎%s讲师上线' % username)
            TEC = techer.Tech(username)
            while 1:
                for index, x in enumerate(TEC.operate_lis, 1):
                    print(index, x[0])
                ch = input('请选择要进行的操作编号：').strip()
                if ch.isdigit() and 0 < int(ch) < 5:
                    ch = int(ch)
                    getattr(TEC, TEC.operate_lis[ch-1][1])()
                else:
                    print('重新选择')

