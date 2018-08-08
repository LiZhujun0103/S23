# 1.将文件中的内容转换成指定格式
com_info = []
with open('a1.txt', 'r', encoding='utf-8') as info:
    first_line = info.readline().split()
    for l in info:
        dic = {}
        for k in range(len(first_line)):
            dic[first_line[k]] = l.split()[k]
        com_info.append(dic)

print(com_info)

# 2.传入函数的字符串中,[数字]、[字母]、[空格]以及[其他]的个数，并返回结果。


def compu(args):        # 不判断中文
    num1 = 0
    lett = 0
    spac = 0
    othe = 0
    for i in args:
        if i.isdigit():
            num1 += 1
        elif i.isalpha():
            lett += 1
        elif i.isspace():
            spac += 1
        else:
            othe += 1

    print("传入的参数中数字%s个，字符%s个，空格%s个，其他字符%s个" % (num1, lett, spac, othe))


compu('ds#we 23f ee3cf )*$')

# 3.写函数，接收两个数字参数，返回比较大的那个数字
def re_max(num1, num2):
    if num1 > num2:
        return num1
    return num2

ret = re_max(19, 18)
print(ret)

# 4.写函数，检查传入字典的value的长度，如果大于2，则仅保留前两个长度的内容
dic = {"k1": "viv1", "k2": [11, 22, 33, 44]}
def re_twe(args):
    for k in args:
        #if len(args[k]) > 2:
         #   args[k] = args[k][0:2]
        args[k] = args[k][0:2]
    return args
print(re_twe(dic))

# 5.写函数接收一个列表类型参数，返回字典
li = [111, 222, 333, 444]

def ch_li(args):
    dic = {}
    for i in range(len(li)):
        dic.setdefault(i, li[i])
    return dic

print(ch_li(li))

# 6.写函数，函数接收四个参数分别是：姓名，性别，年龄，学历
# def in_info(name, sex, age, edu):
#     with open('student_msg', 'a', encoding='UTF-8') as file1:
#         lines = ':'.join([name, sex, age, edu])
#         file1.write(lines+'\n')
#
# name = input("请输入姓名：").strip()
# sex = input("请输入性别：").strip()
# age = input("请输入年龄：").strip()
# edu = input("请输入学历：").strip()
#
# in_info(name, sex, age, edu)

# 7.升级题
#def sj_info(name, age, edu, sex='男'):
#    with open('student_msg', 'a', encoding='UTF-8') as file1:
#        lines = ':'.join([name, sex, age, edu])
#        file1.write(lines+'\n')


#while True:
    # name = input("请输入姓名：").strip()
    # if name.upper() == 'Q':
    #     break
    # sex = input("请输入性别：").strip()
    # age = input("请输入年龄：").strip()
    # edu = input("请输入学历：").strip()
    # if sex == '女':
    #     sj_info(name, age, edu, sex='女')
    # else:
    #     sj_info(name, age, edu)

# 8.修改文件
# import os
# def ch_file(filename, old, new):
#     with open(filename, 'r', encoding='UTF-8') as f1, \
#         open('linshi', 'w', encoding='UTF-8') as f2:
#         for line in f1:
#             if old in line:
#                 line = line.replace(old, new)
#             f2.write(line)
#     os.remove(filename)
#     os.rename('linshi', filename)
#
# ch_file('student_msg', '水', '男')

# 9.回答：代码中,打印出来的值a,b,c分别是什么？为什么？
a = 10
b = 20
def test5(a,b):
    print(a,b)
c = test5(b, a)
print(c)
# 打印出的a为20，b为10，c为None
# 传参过程中时以20为实参传给形参a，以10为实参传给形参b，函数没有设置返回值，默认返回None，所以c打印出来时None
a = 10
b = 20
def test5(a, b):
    a = 3
    b = 5
    print(a, b)
c = test5(b, a)
print(c)
# 打印出a为3，b为5，c为None
# 函数内部有局部变量在函数被调用时会优先使用，函数没有返回值，默认返回None

# 10.写函数,传入函数中多个实参(均为可迭代对象如字符串,列表,元祖,集合等),将每个实参的每个元素依次添加到函数的动态参数args里面
lis = ['a', 'c', 12]
ser = {'ace', 'ida', 'jus'}
dio = {'av': 11, 'df': 'szi'}
def test1(*args):
    print(args)

test1(*lis, *ser, *dio)

# 11.写函数,传入函数中多个实参(实参均为字典),将每个实参的键值对依次添加到函数的动态参数kwargs里面
dic1 = {'abc': 'adc', 'acc': 'aww'}
dic2 = {'sxc': 'awe', 'we': 'pg'}
def test2(**kwargs):
    print(kwargs)

test2(**dic1, **dic2)

# 12.面代码成立么?如果不成立为什么报错?怎么解决
# 题目一
a = 2
def wrapper():
    print(a)
wrapper()
# 成立，打印出a的值2

# 题目二
# a = 2
# def wrapper():
#     a += 1
#     print(a)
# wrapper()
# 不成立，会报错；a是全局作用域变量，局部作用域未经声明修改其值会报错，在局部作用域用global a

# 题目三
def wrapper():
    a = 1
    def inner():
        print(a)
    inner()
wrapper()
# 成立，打印出a的值1

# 题目四
# def wrapper():
#     a = 1
#     def inner():
#         a += 1
#         print(a)
#     inner()
# wrapper()
# 不成立，会报错，inner函数局部作用域的a无法修改到上一层函数的a，可用nolocal a解决

# 13.写函数,接收两个数字参数,将较小的数字返回
def max_num(x, y):
    z = x if x > y else y
    return z

print(max_num(34, 78))

# 14.写函数,接收一个参数(此参数类型必须是可迭代对象),将可迭代对象的每个元素以’_’相连接,形成新的字符串,并返回
lis1 = ['a', 'd', 'e', 'x']
def spl(*args):
    slt = []
    for i in args:
        slt.append(str(i))
    xman = '_'.join(slt)
    return xman

print(spl(*lis1))

# 15.写函数，传入n个数，返回字典{‘max’:最大值,’min’:最小值}
def re_max(*args):
    dicx = {}
    dicx['max'] = max(args)
    dicx['min'] = min(args)
    return dicx
print(re_max(11, 22, 3, 4))

# 16.写函数，传入一个参数n，返回n的阶乘
def jx(x):
    if x == 1:
        return 1
    else:
        return x * jx(x-1)

print(jx(7))

# 17.写函数，返回一个扑克牌列表，里面有52项，每一项是一个元组
li1 = ['红心', '黑桃', '方块', '梅花']
li2 = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
ll = []
for i in range(len(li1)):
    for x in range(len(li2)):
        ll.append((li1[i], li2[x]))
print(len(ll))
print(ll)

# 18.
def wrapper():
    def inner():
        print(666)
    inner()

wrapper()

def wrapper():
    def inner():
        print(666)
    return inner

wrapper()()