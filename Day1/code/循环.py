# while True: # 无限循环
#     print("死了都要爱")
#     print("学猫叫")
#     print("吹口哨")
#     print("男儿当自强")

'''
while 条件:
    代码块(循环体)
    
执行流程：
    判断条件是否为真， 如果真， 执行循环体，然后再次判断条件是否为真。直到条件为假。循环终止
'''
# 用循环进行数数 1-100
# count = 1
# while count <= 100:
#     print(count)
#     count = count + 1

# 计算1+2+3+4+5+6+7+....100=?
# count = 1
# sum = 0
# while count <= 100:
#     sum = sum + count   # 把每次循环的值进行累加记录
#     count = count + 1
# print(sum)


# 请用户输入内容。如果输入的是q程序退出
# while True: # 死循环
#     content = input("请输入一个内容：")
#     if content == "q":
#         break   # 停止，终止， 打断循环
#     else:
#         print("你输入的内容是", content)
# print("我是其他")

while True:
    content = input("请输入一个内容：")
    if content == "q":
        print("这里是continue之前")
        continue    # 终止当前本次循环。 继续执行下一次循环
        pirnt("这里是continue之后")
    print("你输入的内容是：", content)

# break 和 continue
# break 彻底终止这个循环
# continue 终止当前本次循环。继续执行下一次循环


