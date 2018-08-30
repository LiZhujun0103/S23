import re
del_space = lambda st : re.sub('\s+', '', st)       # 利用匿名函数去除字符串中的空格

def fomt(xxx):                      # 测试过程中发现会有双符号的情况出现，需要处理一下,replace()匹配不到的话会返回原字符串
    conn = xxx.replace('+-', '-')           #  开始写错这个地方，查了好久。。。
    conn = conn.replace('--', '+')
    conn = conn.replace('-+', '-')
    conn = conn.replace('++', '+')
    return conn

def mult_div(con):                                  # 计算乘除法的函数，分割符号判断是乘法还是除法
    m1 = re.findall('[*/]', con)
    m2 = re.split('[*/]', con)
    summ = 0
    for z, x in enumerate(m2):
        if summ:
            if m1[z-1] == '*':
                summ *= float(x)
            elif m1[z-1] == "/":
                summ /= float(x)
        else:
            summ = float(x)
    return summ

def calc(con):                                  # 计算表达式，先乘除后加减
    conn = con.strip('()')
    conn = fomt(conn)
    c1 = re.findall('[-+]', conn)
    c2 = re.split('[-+]', conn)
    if c2[0] == '':                                 # 第一个数时负数的时候，调整一下格式
        c2[1] = '-%s' % c2[1]
        del c2[0]
        del c1[0]
    for c, v in enumerate(c2):
        if v.endswith('*') or v.endswith('/'):          # 测试过程中发现有乘除符号和加减符号有挨着的情况，处理一下
            c2[c] = v + str(c1[c]) + '%s' % c2[c+1]
            del c1[c]
            del c2[c+1]
    for j, k in enumerate(c2):
        rest = mult_div(k)                              # 乘除法计算出结果后替换回去
        c2[j] = rest
    sun = 0
    for r, e in enumerate(c2):                          # 加法运算
        if sun:
            if c1[r-1] == '+':
                sun += float(e)
            elif c1[r-1] == '-':
                sun -= float(e)
        else:
            sun = float(e)
    return sun

def main(con):                              # 主执行函数
    conn = del_space(con)                   # 去空格
    last_con = 0
    flag = 1
    while flag:
        kuohao = re.search('\([^\()]+\)', conn)             # 过滤出最内层小括号
        if kuohao:
            kuohao_after = calc(kuohao.group())             # 计算出最内层小括号的值
            conn = conn.replace(kuohao.group(), str(kuohao_after))      # 内层小括号的值替换到字符串中，进行下一轮循环
        else:
            last_con = calc(conn)
            flag = 0
    return last_con


str11 = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
asdf = main(str11)
print(asdf)