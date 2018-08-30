# 1.new方法和init方法的执行顺序
# __new__方法的调用是发生在__init__之前；__new__ 通常用于控制生成一个新实例的过程。它是类级别的方法。
# __init__ 通常用于初始化一个新实例，控制这个初始化的过程，比如添加一些属性， 做一些额外的操作，发生在类实例被创建完以后。
# 它是实例级别的方法。

# 2.call方法在什么时候被调用
# 将类实例化为对象之后，在对象后面跟一个()执行的时候，就是在调用call方法

# 3.用反射为类添加一个静态属性
class test1:
    def __init__(self):
        print('This is class test1')

t1 = test1()
setattr(t1, 'attrb', 'abcd123')
print(t1.attrb)

# 4.用反射为上题的类的对象添加一个属性name,值为你的名字
getattr(t1, 'name', setattr(t1, 'name', 'lizhujun'))
print(t1.name)

# 5.请使用new方法实现一个单例模式
class test2:
    def __init__(self):
        print('This is test2')

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'ins'):
            cls.ins = object.__new__(cls, *args, **kwargs)
        return cls.ins

t2 = test2()
t3 = test2()
t2.tt = 'abc'
print(t3.tt)

# 6.校验两个文件的一致性
import hashlib
with open('testfile1', 'w', encoding='utf8') as f1, open('testfile2', 'w', encoding='utf8') as f2:
    f1.write('这是测试文件内容')
    f2.write('这是测试文件')

def get_file(file):
    md5 = hashlib.md5()
    while 1:
        data = file.read(1024)
        if data:
            md5.update(data)
        else:
            break
    return md5.hexdigest()

with open('testfile1', 'rb') as f3, open('testfile2', 'rb') as f4:
    file1_md5 = get_file(f3)
    file2_md5 = get_file(f4)
    print(file1_md5)
    print(file2_md5)
    if file1_md5 == file2_md5:
        print('%s和%s是相同文件' % ('testfile1', 'testfile2'))
    else:
        print('两个文件不一致')

# 7.加盐的密文登录
import random
def create_salt():
    salt = ''
    for i in range(5):
        num = random.randint(0, 9)
        char = chr(random.randint(65, 90))
        add = random.choice([num, char])
        salt = ''.join([salt, str(add)])
    return salt

def create_md5(pwd, salt):
    md5 = hashlib.md5()
    md5.update((pwd+salt).encode('utf8'))
    return md5.hexdigest()

salt = create_salt()
pawd = input('请输入密码（任意字符）：').strip()
md5_pass = create_md5(pawd, salt)
print('原始密码为%s' % pawd)
print('salt值为：%s' % salt)
print('加盐后的密文为：%s' % md5_pass)

# 8.完成一个既可以向文件输出又可以向屏幕输出的日志设置
import logging
log_dir = 'record.log'
def get_logger(log_dir):
    logger = logging.getLogger()                                            # 获得一个logger对象，默认是root
    fh = logging.FileHandler(log_dir,encoding='utf-8')                      #创建一个文件流并设置编码utf8
    ch = logging.StreamHandler()
    logger.setLevel(logging.DEBUG)                                          #设置最低等级debug
    fm = logging.Formatter("%(asctime)s --- %(message)s")                   #设置日志格式
    fh.setFormatter(fm)                                                     # 把文件流添加写入格式
    ch.setFormatter(fm)
    logger.addHandler(fh)                                                   #把文件流添加进来，流向写入到文件
    logger.addHandler(ch)
    return logger


loggs = get_logger(log_dir)
loggs.debug('debug message')
loggs.info('info message')
loggs.warn('warn message')
loggs.error('error message')
loggs.critical('critical message')
