# 1.有变量name = "aleX leNb"完成下列操作：
name = "aleX leNb"
# 1)移除变量两边的空格，并输出
print(name.strip())
# 2)移除name变量左边的"al"并输出
print(name.lstrip('al'))
# 3)移除name变量右面的"Nb"并输出
print(name.rstrip('Nb'))
# 4)移除name变量开头的a与最后的b并输出
print(name.lstrip('a').rstrip('b'))
# 5)判断name变量是否以"al"开头并输出
print(name.startswith('al'))
# 6)判断name变量是否以"Nb"结尾并输出
print(name.endswith('Nb'))
# 7)将name变量对应的值中的所有的"l"替换成"p"并输出
name = name.replace('l', 'p')
print(name)
# 8)将name变量对应的值中的第一个"l"替换成"p"并输出
name = "aleX leNb"
name = name.replace('l', 'p', 1)
print(name)
# 9)将name变量对应的值根据所有的"l"分割并输出
name = "aleX leNb"
print(name.split('l'))
# 10)将name变量对应的值根据第一个"l"分割并输出
name = "aleX leNb"
print(name.split('l', maxsplit=1))
# 11)将name变量对应的值变大写并输出
print(name.upper())
# 12)将name变量对应的值变小写并输出
print(name.lower())
# 13)将name变量对应的值首字母"a"大写并输出
print(name.capitalize().replace('n', 'N'))
# 14)判断name变量对应的值字母"l"出现几次并输出
print(name.count('l'))
# 15)判断name变量对应的值前四位"l"出现几次并输出
print(name.count('l', 0, 3))
# 16)从name变量对应的值中找到"N"对应的索引（如果找不到报错）
print(name.index('N'))
# 17)从name变量对应的值中找到"N"对应的索引（如果找不到返回-1）
print(name.find('N'))
# 18)从name变量对应的值中找到"X le"对应的索引并输出
#print(name.index('X le'))
print(name.find('X le'))
# 19)输出name变量对应的值的第2个字符
print(name[1])
# 20)输出name变量对应的值的前3个字符
print(name[0:3])
# 21)输出name变量对应的值的后2个字符
print(name[-2:])
# 22)输出name变量对应的值中"e"所在索引位置
print(name.index('e'))

# 2.有字符串s="123a4b5c"
s = "123a4b5c"
# 1)通过对s切片形成新的字符串s1,s1 = "123"
s1 = s[0:3]
print(s1)
# 2)通过对s切片形成新的字符串s2,s2 = "a4b"
s2 = s[3:6]
print(s2)
# 3)通过对s切片形成新的字符串s3 s3 = "1345"
s3 = s[0::2]
print(s3)
# 4)通过对s切片形成字符串s4 s4="2ab"
s4 = s[1:6:2]
print(s4)
# 5)通过对s切片形成s5, s5 = "c"
s5 = s[-1]
print(s5)
# 6)通过对s切片形成字符串s6, s6 = "ba2"
s6 = s[-3::-2]
print(s6)

# 3.使用while或for循环分别打印字符串s="asdfer"中每个元素
s = "asdfer"
for x in s:
    print(x)

# 4.使用for循环对s="asdfer"进行循环，但是每次打印的内容都是"asdfer"
s = "asdfer"
for i in s:
    print(s)

# 5.使用for 循环对s="abcdefg"进行循环，每次打印的内容是每个字符加sb
s = "abcdefg"
for e in s:
    print(e + "sb")

# 6.使用for循环对s="321"进行循环，打印的内容依次是"倒计时3秒..."
s = "321"
for i in s:
    print("倒计时%s秒" % i)
else:
    print("出发!")

# 7.实现一个整数加法计算器(两个数相加)
content = input("请输入加法计算表达式(两数相加):").strip()
alis = content.split('+')
a = alis[0]
b = alis[1]
c = int(a) + int(b)
print(content, "=", c)

# 8.整数加法计算器（多个数相加）
content = input("请输入计算表达式(多数相加):").strip().replace(" ", "")
alis = content.split('+')
c = 0
for n in alis:
    c += int(n)
print(content, "=", c)

# 9.计算用户输入的内容中有几个整数（以个位数为单位）
content = input("请输入内容：").strip()
co = 0
for i in content:
    if i.isdigit():
        co += 1

print("内容中有整数%d个" % co)

# 10. 写一个选择回家的小程序
while 1:
    user_ch = input("回家方式请选择A/B/C:").strip().upper()
    if user_ch == 'A':
        print("走大路回家")
        user_tol = input("选择公交按1，选择步行按2:").strip()
        if user_tol == '1':
            print("10分钟到家")
            break
        elif user_tol == "2":
            print("20分钟到家")
            break
    elif user_ch == "B":
        print("走小路回家")
        break
    elif user_ch == "C":
        print("绕道回家")
        user_tol = input("选择游戏厅玩会按1，选择网吧按2：").strip()
        if user_tol == '1':
            print("一个半小时到家，爸爸在家，拿棍等你")
            continue
        elif user_tol == '2':
            print("两个小时到家，妈妈已经做好战斗准备")
            continue
    else:
        print("请重新输入")

# 11.计算1-2+3-4..+99除了88之外的所有数的总和
number = 1
Sum = 0
while number < 100:
    res = number % 2
    if res == 1:
        Sum += number
        number += 1
    else:
        if number != 88:
            Sum -= number
            number += 1
        else:
            number += 1
else:
    print("1-2+3-4..+99除了88之外的所有数的总和为%d" % Sum)

# 16.输入用户名、地点、爱好
user_name = input("请输入姓名：").strip()
user_pass = input("请输入爱好：").strip()
user_addr = input("请输入地点：").strip()
print("Hi,亲爱的%s，听说你喜欢去%s%s" % (user_name, user_addr, user_pass))

# 17.敏感字符检测
flag = 1
Sensitive = ["粉嫩", "铁锤"]
while flag:
    content = input("请输入你的内容(敏感检测)：")
    for i in Sensitive:
        if i in content:
            print("注意你的言辞，请重新输入")
            break
    else:
        print(content)
        flag = 0

# 18. 写代码完成需求
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# 1)计算列表长度
print(len(li))
# 2)列表中追加元素"seven"
li.append("seven")
print(li)
# 3)在列表的第一个位置插入"tony"
li.insert(0, "tony")
print(li)
# 4)修改列表第二个位置元素为"kelly"
li[1] = "kelly"
print(li)
# 5)更新列表
l2 = [1, "a", 3, 4, "heart"]
li.extend(l2)
print(li)
# 6)
s = "qwert"
li.extend(s)
print(li)
# 7)删除列表中的元素"eric"
# li.remove('eric')
# print(li)
# 8)删除列表中第2个元素
cal = li.pop(1)
print(cal, li)
# 9)删除列别第2到4个元素
del li[1:4]
print(li)
# 10)反转列表
li.reverse()
print(li)
# 11)统计"alex"出现的次数
li = ['alex', 'WuSir', 'ritian', 'barry', 'wenzhou']
print(li.count('alex'))

# 19.利用切片实现功能
li = [1, 3, 2, "a", 4, "b", 5, "c"]
# 1)形成新列表l1=[1, 3, 2]
l1 = li[0:3]
print(l1)
# 2)形成新列表l2=['a', 4, 'b']
l2 = li[3:6]
print(l2)
# 3)形成新列表l3=[1, 2, 4, 5]
l3 = li[0::2]
print(l3)
# 4)形成新列表l4=[3, "a", "b"]
l4 = li[1:6:2]
print(l4)
# 5)形成新列表l5=["c"]
l5 = li[-1]
print(l5)
# 6)形成新列表l6=["b", "a", 3]
l6 = li[-3::-2]
print(l6)

# 20.根据列表实现功能
lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# 1)将列表中的tt变为大写（两种方式）
lis[3][2][1][0] = "TT"
print(lis)
lis[3][2][1][0].upper()
print(lis)
# 2)将列表中的数字3变成字符串"100"(两种方法)
lis[1] = "100"
lis[3][2][1][1] = "100"
print(lis)
lis[3][2][1].pop(1)
lis[3][2][1].insert(1, "100")
print(lis)
# 3)将列表中的字符串1修改为数字101
lis[3][2][1][2] = 101
print(lis)
lis[3][2][1].pop(2)
lis[3][2][1].insert(2, 101)
print(lis)

# 21.拼接字符串
li = ["alex", "eric", "rain"]
a = "_".join(li)
print(a)

# 22.利用for和range打印列表索引
li = ['alex', 'WuSir', 'ritian', 'barry', 'wenzhou']
for i in range(len(li)):
    print(i)

# 23 .利用for和range找出100以内所有偶数并插入到新列表中
li = []
for i in range(0, 100, 2):
    li.append(i)
print(li)

# 24.利用for和range找出50以内能被3整除的数并插入到新列表
nli = []
for x in range(50):
    if x % 3 == 0:
        nli.append(x)
print(nli)

# 25.利用for和range打印100-1
for i in range(100, 0, -1):
    print(i)

# 26. 利用for循环和range从100~10，倒序将所有的偶数添加到一个新列表中，然后对列表的元素进行筛选，将能被4整除的数留下来
li1 = []
for i in range(100, 10, -2):
    li1.append(i)
for x in li1:
    if x % 4 != 0:
        li1.remove(x)
print(li1)

# 26.利用for循环和range，将1-30的数字一次添加到一个列表中，并循环这个列表，将能被3整除的数改成*
li2 = []
li3 = []
for i in range(1, 31):
    li2.append(i)
for x in li2:
    if x % 3 != 0:
        li3.append(x)
    else:
        li3.append("*")
li2 = li3
print(li2)

# 27.查找列表li中的元素，移除每个元素的空格，并找出以"A"或者"a"开头，并以"c"结尾的所有元素，并添加到一个新列表中, 最后循环打印这个新列表
li = ["TaiBai ", "alexC", "ABC ", "egon", " riTiAn", "WuSir", "  aqc"]
li5 = []
for i in li:
    if i.strip().upper().startswith('A') and i.strip().endswith('c'):
        li5.append(i.strip())
for x in li5:
    print(x)

# 28.开发敏感词语过滤程序，提示用户输入评论内容
li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
content = input("请输入评论(例如：听说苍老师经常再东京热看见武藤兰和波多野结衣一起拍电影)：").strip()
for i in li:
    if i in content:
        content = content.replace(i, '*'*len(i))
content = content
print(content)

# 29. 有如下变量（tu是个元祖），请实现要求的功能
# a)元组特性
# 1）元组是一个只读列表，只可以查看，不可以修改增加和删除；
# 2）在定义只有一个元素的元组时，要加上逗号以示和小括号的区别，如 age = (28, )
# b)请问tu变量中的第一个元素"alex"是否可被修改？
# 元组是不可变列表，tu的第一个元素"alex"是字符串，不可被修改
# c)tu中的k2对应值是列表，列表的元素可以修改
tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}, 44])
tu[1][2]["k2"].append("Seven")
print(tu)
# d)tu中k3对应的值是元组类型，不能修改

# 30.字典dic
dic = {'k1': "v1", "k2": "v2","k3": [11, 22, 33]}
# a)循环输出所有key
for i in dic.keys():
    print(i)
# b)循环输出所有的value
for i in dic.keys():
    print(dic[i])
# c)循环输出所有的key/value
for k, v in dic.items():
    print(k, v)
# d)添加一个键值对k4:v4
dic["k4"] = "v4"
print(dic)
# e)修改k1的值为alex
dic["k1"] = "alex"
print(dic)
# f)在k3对应的值中添加一个44
dic["k3"].append(44)
print(dic)
# g)在k3对应的值第一个位置插入18
dic["k3"].insert(0, 18)
print(dic)

# 31. 如下
av_catalog = {
    "欧美": {
        "www.youporn.com": ["很多免费的,世界最大的", "质量一般"],
        "www.pornhub.com": ["很多免费的，也很大", "质量比youporn高点"],
        "letmedothistoyou.com": ["多是自拍,高质量图片很多", "资源不多，更新慢"],
        "x-art.com": ["质量很高，真的很高", "全部收费，屌丝请绕过"]
    },
    "日韩": {
        "tokyo-hot": ["质量怎样不清楚，个人已经不喜欢日韩范了", "verygood"]
    },
    "大陆": {
        "1024": ["全部免费，真好，好人一生平安", "服务器在国外,慢"]
    }
}

# a 给此["很多免费的,世界最大的","质量一般"]列表第二个位置插入一个元素：'量很大'
av_catalog["欧美"]["www.youporn.com"].insert(1, "量很大")
print(av_catalog)
# b 将此["质量很高,真的很高","全部收费,屌丝请绕过"]列表的"全部收费,屌丝请绕过" 删除。
av_catalog["欧美"]["x-art.com"].pop(1)
print(av_catalog)
# d 将此["质量怎样不清楚,个人已经不喜欢日韩范了","verygood"]列表的"verygood"全部变成大写
av_catalog["日韩"]["tokyo-hot"][1] = av_catalog["日韩"]["tokyo-hot"][1].upper()
print(av_catalog)
# e 给'大陆'对应的字典添加一个键值对'1048' :['一天就封了']
av_catalog["大陆"]["1048"] = ["一天就封了"]
print(av_catalog)
# f 删除此"letmedothistoyou.com": ["是自拍,高质量图片很多","资源不多,更新慢"]键值对
av_catalog["欧美"].pop("letmedothistoyou.com")
print(av_catalog)
# g 给此["全部免费,真好,好人一生平安","服务器在国外,慢"]列表的第一个元素，加上一句话：'可以爬下来'
av_catalog["大陆"]["1024"].insert(0, "可以爬下来")
print(av_catalog)

# 32.字符串"k:1|k1:2|k2:3|k3:4" 处理成字典{'k':1,'k1':2....}
s1 = "k:1|k1:2|k2:3|k3:4"
l1 = s1.split("|")
d1 = {}
for i in l1:
    w = i.split(":")
    d1[w[0]] = w[1]
print(d1)

# 33. 有如下值
# li= [11,22,33,44,55,66,77,88,99,90]，将所有大于66 的值保存至字典的第一个key中，将小于66 的值保存至第二个key的值中
li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
dic1 = {}
for i in li:
    if i > 66:
        dic1.setdefault("k1", []).append(i)
    elif i < 66:
        dic1.setdefault("k2", []).append(i)
print(dic1)
