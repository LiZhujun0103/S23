# 1.简述类、对象、实例化、实例分别是什么
# 类：具有相同特征的一类事物  抽象的，不可具体描述
# 对象／实例：具体的某一个事物   可具体详细描述的
# 实例化：将类转变为一个实例的过程叫做实例化

# 2.面向对象的三大特性
# 继承、多态、封装

# 3.python中的封装是什么意思
# （还没学，查了下资料）
# 封装是：隐藏对象的属性和实现细节，仅对外提供公共访问方式

# 4.多态是什么，在python中如何体现
# 可以对不同类的对象使用相同操作   （还不是很清楚这块，在学习）

# 5.面向对象中，‘私有’的概念
# 面向对象的私有成员,他们只能在类的内部使用,不能再类的外部以及派生类中使用

# 6/7题还不会，学习后补上

# 8.下面代码会输出 in son，因为子类和父类存在同名方法时，子类优先调用自己的方法
class Foo:
    def func(self):
        print('in father')

class Son(Foo):
    def func(self):
        print('in son')

s = Son()
s.func()


# 正则
# 1.匹配整数或者小数
import re
a1 = '-3.14s15sdd'
s1 = re.compile('-?\d+\.?\d*')
ret1 = s1.findall(a1)
print(ret1)

# 2.匹配年月日日期格式
a2 = 'dsd2018-8-22dg'
s2 = re.compile('\d{4}-\d{1,2}-\d{1,2}')
ret2 = s2.findall(a2)
print(ret2)

# 3.匹配QQ号
a3 = 'dc0837549832fs343f'
s3 = re.compile('[1-9]\d{5,11}')
ret3 = s3.findall(a3)
print(ret3)

# 4.匹配11位电话号码
a4 = '13713249090'
s4 = re.compile('^(?:13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$')
ret4 = s4.findall(a4)
print(ret4)

# 5.长度为8到10的密码
a5 = 'asdREr34_s'
s5 = re.compile('^\w{8,10}$')
ret5 = s5.findall(a5)
print(ret5)

# 6.匹配验证码 4位数字字母
a6 = '6Y8d'
s6 = re.compile('^[0-9a-zA-Z]{4}$')
ret6 = s6.findall(a6)
print(ret6)

# 7.匹配邮箱地址
a7 = 'dsa.i_32ds@dew23.com'
s7 = re.compile('^[\w\-?]+(?:\.[\w\-?]+){0,4}@[\w\-?]+(?:\.[\w\-?]+){0,4}')
ret7 = s7.findall(a7)
print(ret7)

# 8.
a8 = '''<a>wahaha</a>
<b>banana</b>
<h1>qqxing</h1>'''
s8 = re.compile('<\w+>(.*)</\w+>')
s88 = re.compile('<(?P<tnm>\w+)>.*</(?P=tnm)>')
ret8 = s8.findall(a8)
ret88 = s88.findall(a8)
print(ret8)
print(ret88)

# 9 1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))
# 1)从上面算式中匹配出最小层括号以及小括号内的表达式
str1 = '1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'
st1 = re.compile('\(([^()]+)\)')
st2 = re.compile('\((?:[^()]+)\)')
rr1 = st1.findall(str1)
rr2 = st2.findall(str1)
print(rr1)
print(rr2)
# 10 从类似9-2*5/3+7/3*99/4*2998+10*568/14的表达式中匹配出从左到右第一个乘法或除法
str2 = '9-2*5/3+7/3*99/4*2998+10*568/14'
st2 = re.compile('\d+\.?\d*[*,/]\d+')
rr2 = st2.search(str2)
print(rr2.group())

# 11 匹配一篇英文文章的标题 类似The Voice Of China
str3 = 'The Voice Of China And CN'
st3 = re.compile('[a-zA-Z]+\s?(?:[a-zA-Z]+\s?)+')
rr3 = st3.findall(str3)
print(rr3)

# 12 匹配一个网址
str4 = 'https://www.nbanb.com.cn'
st4 = re.compile('^[(https|http|ftp)?:\/\/][^\s]+')
rr4 = st4.findall(str4)
print(rr4)

# 13 匹配年月日日期 类似 2018-12-06 2018/12/06 2018.12.06
str5 = '2018-12.06'
st5 = re.compile('\d{4}[\-,\/,\.]\d{1,2}[\-,\/,\.]\d{1,2}')
rr5 = st5.findall(str5)
print(rr5)

# 14 匹配15位或18位身份证号
str6 = '11032520051106007x'
st6 = re.compile('\d{17}[\d|x]|\d{15}')
rr6 = st6.findall(str6)
print(rr6)

# 15 匹配lianjia.html中信息
import json
with open('lianjia.html', mode='r', encoding='utf8') as ff:
    lianj = ff.read()
st7 = re.compile('"">(.*?)</a>.*?<span class="divide">/</span>(.*?)<span class="divide">/</span>(.*?)<span class="divide">/</span>', re.S)
rr7 = st7.findall(lianj)
print(rr7)

