
# 第一题：简述变量命名规范
# 1.变量由字母、数字和下划线搭配组成
# 2.不可以用数字开头，更不能全部是数字
# 3.不能用python的关键字
# 4.命名要有意义
# 5.不要使用中文
# 6.不要太长
# 7.区分大小写
# 8.尽量使用驼峰体或下划线组合

# 第二题：name = input(“>>>”) name变量量是什什么数据类型？
# input获取得到的均为字符串类型(str)

# 第三题：if条件语句的基本结构
# 语法1
# if 条件:
#     结果
#
# 语法2
# if 条件:
#     结果1
# else:
#     结果2
#
# 语法3
# if 条件1:
#     结果1
# elif 条件2:
#     结果2
# ...
# else:
#     结果n
#
# 语法4
# if 条件1:
#     结果1
#     if 条件2:
#         结果2
#     else:
#         结果3
# else:
#     结果4

# 第四题：用print打印出内容
content = '''问能提笔安天下,
武能上马定乾坤.
心存谋略何人胜,
古今英雄唯是君'''
print(content)

# 第五题：利用if语句写出猜大小的游戏

guessNumber = 66
while True:
    yourNumber = input('请输入你猜测的数字：')
    yourNumber = int(yourNumber)
    if yourNumber == guessNumber:
        print('Your are right, very good!')
        break
    elif yourNumber > guessNumber:
        print('Your number bigger!')
    else:
        print('Your number smaller!')

# 第六题：提⽰⽤用户输入他的年年龄, 程序进⾏行行判断

userAge = input('请输入你的年龄：')
userAge = int(userAge)
if userAge <= 10:
    print('小屁孩')
elif 10 < userAge <= 20:
    print('青春期叛逆的小屁孩')
elif 20 < userAge <= 30:
    print('开始定性，开始混社会的小屁孩儿')
elif 30 < userAge <= 40:
    print('看老大不小了，赶紧结婚小屁孩儿')
elif 40 < userAge <= 50:
    print('家里有个不听话的小屁孩儿')
elif 50 < userAge <= 60:
    print('自己马上变成不听话的老屁孩儿')
elif 60 < userAge <= 70:
    print('活着还不错的老屁孩儿')
elif 70 < userAge <= 90:
    print('人生就快结束了的一个老屁孩儿')
elif userAge > 90:
    print('再见了这个世界')

# 第七题：单行注释和多行注释
# 在"#"后面的内容为单行注释的内容
# 多行注释用三个引号将内容引起来
# 这是单行注释的内容
'''这是多行
注释掉的
内容'''

# 第八题：python2和python3的区别
# 1.print语句被python3废弃，统一使用print函数
# 2.long整数类型被Python3废弃，统一使用int
# 3.raw_input函数被Python3废弃，统一使用input函数
# 4.Python2:/是整数除法，//是小数除法；Python3:/是小数除法，//是整数除法
# 5.Python2中任意两个对象都可以比较；Python3中只有同一数据类型的对象可以比较


# 第九题：提示用户输入麻花藤
username = input('请输入名称"麻花藤"：')
if username == '麻花藤':
    print('非常聪明')
else:
    print('你是傻逼么')

# 第十题:使用while循环输出1 2 3 4 5 6  8 9 10
num = 1
while num <= 10:
    if num == 7:
        num += 1
        continue
    print(num)
    num += 1

# 第十一题:求1-100所有数的和
# 法一：
Total = 0
numbers = 1
while numbers <= 100:
    Total = Total + numbers
    numbers += 1

print("1-100所有数的和为：", sum) #粗心了，之前上面循环用了个sum,后来发现不对，上面改成Total，下面忘记改了
# 法二：偷师学到点函数，练习一下


def all_number(i):
    sums = 0
    if i == 1:
        return 1
    else:
        sums = i + all_number(i-1)
        return sums


print(all_number(100))

# 第十二题: 输出1-100内所有奇数
odd_number = 1
while odd_number <= 100:
    odd_res = odd_number % 2
    if odd_res == 1:
        print(odd_number)
    odd_number += 1

# 第十三题：输出1-100内所有的偶数
even_number = 1
while even_number <= 100:
    even_res = even_number % 2
    if even_res == 0:
        print(even_number)
    even_number += 1

# 第十四题：求1-2+3-4+5 ... 99的所有数的和
number = 1
Sum = 0

while number <= 100:			#是计算到99，不是到100
    res = number % 2
    if res == 1:
        Sum += number
        number += 1
        continue
    else:
        Sum -= number
        number += 1
        continue

print(Sum)
