# 1.计算两个格式化时间之间差了多少年月日时分秒
import time
time_one = '2018-08-15 15:35:48'
time_two = '2029-02-09 11:24:26'
time_1 = time.mktime(time.strptime(time_one, '%Y-%m-%d %H:%M:%S'))
time_2 = time.mktime(time.strptime(time_two, '%Y-%m-%d %H:%M:%S'))
tm_ret = time_2 - time_1
tm_ft = time.gmtime(tm_ret)
print('两个日期相差%s年%s月%s日%s小时%s分钟%s秒' % (tm_ft.tm_year-1970, tm_ft.tm_mon-1, tm_ft.tm_mday-1,
                                      tm_ft.tm_hour, tm_ft.tm_min, tm_ft.tm_sec))

# 2.计算当前时间所在月1号的时间戳
mon = time.strftime('%Y-%m', time.localtime())
mf = time.strptime(mon, '%Y-%m')
ch = time.mktime(mf)
print('本月1号的时间戳为%s' % ch)


# 3.生成一个6位随机验证码（包含数字和字母）
import random
def rans(n=6):
    li = ''
    for i in range(n):
        lw = chr(random.randint(97, 122))
        up = chr(random.randint(65, 90))
        nu = str(random.randint(0, 9))
        li += random.choice([lw, up, nu])
    return li

aa = rans()
print(aa)

# 4.发红包，制定金额和个数随机分配红包金额
#  此题查了好多资料,不太理解让每次随机的概率相同的那块算法
def redbag(total, num):
    total = float(total)
    num = int(num)
    mini = 0.01
    n = 1
    while num > n:
        maxx = total - mini * (num - 1)
        if (num - 1) <= 2:
            maxx = maxx / num
        maxx = maxx / (num - 1) * 2              #二倍均值法随机取数，保证每次随机金额的平均值相等;随机区间为： （最小值，金额/数量*2）
        mon = random.randint(int(mini)*100, int(maxx)*100)
        mon = float(mon)/100
        total -= mon
        print('第%d个抢到红包的金额为%.2f' % (n, mon))
        n += 1
    print('第%d个抢到红包的金额为%.2f' % (n, total))

redbag(500, 6)


# 5.分别列出给定目录下所有文件和文件夹
import os
a = os.listdir(r'D:')
print(a)

# # 6.获取当前文件所在目录
b = os.getcwd()
print(b)

# # # 7.在当前目录下创建一个文件夹,在这个文件夹下再创建一个文件夹
# os.makedirs('dir1/dir11')
#
# 8.计算某路径下文件个文件夹的大小的总和
def getsizes(dir):
    size = 0
    for r, d, f in os.walk(dir):
        sizelist = [os.path.getsize(os.path.join(r, name)) for name in f]
        size += sum(sizelist)
    return size

ss = getsizes(r'../../')/1024
print('目录内文件和文件夹的总大小为: %.2f KB' % ss)