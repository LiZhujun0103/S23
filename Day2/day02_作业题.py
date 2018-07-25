#! -*- coding:utf8 -*-
# Author: ZhuJun.li

buy_car = []                    # 定义一个空列表作为购物车
nbuy_car =[]                    # 定义一个中转用的列表，在使用到的时候再定义也可
record_car = []                 # 定义一个列表作为购物车结算后再购物后退出时统计使用
buy_money = 0                   # 定义消费金额初始值
filt_car = {}                   # 定义一个空字典，结算购物车时计数使用
flag = 1                        # 设定一个标识位，while循环使用
goods_list = [                  # 定义商品列表
    ("苹果电脑", 8000),
    ("华为手机", 4999),
    ("巴黎世家", 3999),
    ("象印水杯", 1999)
]
recharge = input("请输入充值金额：").strip()
if recharge.isdigit():
    recharge = int(recharge)
    while flag:
        flag1 = 1
        for k, v in enumerate(goods_list, 1):                       # 利用enumerate打印商品列表及编号
            print(k, v[0], v[1])
        print("n 结算购物车")
        print("q 退出程序")
        choise_id = input("请选择要购买的商品编号：").strip()
        if choise_id.isdigit():
            choise_id = int(choise_id)
            if choise_id >= 0 and choise_id <= len(goods_list):      # 判断输入的合法
                choise_id -= 1
                buy_car.append(goods_list[choise_id])
                print("您已将%s添加到购物车，其单价为%d" % (goods_list[choise_id][0], goods_list[choise_id][1]))
                print("欢迎继续购物".center(50, '*'))
            else:
                print("输入错误，请重新选择商品编号")
        elif choise_id.upper() == 'N':
            while flag1:
                for i in buy_car:                                   # 统计每个商品买了多少个
                    filt_car.setdefault(i, buy_car.count(i))
                for x in filt_car:
                    buy_money += x[1] * filt_car[x]                 # 计算需要消费金额
                if recharge >= buy_money:
                    print("您本次结算的商品如下：")
                    for n in filt_car:
                        print(n[0], filt_car[n], n[1])
                    recharge -= buy_money
                    record_car.extend(buy_car)                      # 购买成功之后将商品添加到记录列表，给后面退出时使用
                    buy_car = []                                    # 结算后清空购物车，方便继续购买
                    filt_car = {}
                    flag1 = 0
                    go_buy = input("输入q退出程序，输入其他任意键继续购物").strip().upper()
                    if go_buy == "Q":
                        flag = 0
                        for u in record_car:
                            filt_car.setdefault(u, record_car.count(u))
                        print("您本次成功购买了如下商品：")
                        for s in filt_car:
                            print(s[0] + " 总共" + str(filt_car[s]) + "个" + ",每个单价为" + str(s[1]))
                        print("您本次一共消费%s元，还剩余额%s元" % (buy_money, recharge))
                    else:
                        continue
                else:
                    print("您的余额不足，请移除购物车中部分商品，当前购物车中商品如下：")
                    for o in buy_car:
                        if o not in nbuy_car:
                            nbuy_car.append(o)
                    for q, w in enumerate(nbuy_car, 1):
                        print(q, w[0] + " 数量:" + str(filt_car[w]))
                    del_goods = input("请选择您要移除的商品编号：").strip()      # 余额不足时移除商品，然后重新计算是否够买
                    if del_goods.isdigit():
                        del_goods = int(del_goods)
                        if del_goods > 0 and del_goods <= len(nbuy_car):
                            del_goods -= 1
                            buy_car.remove(nbuy_car[del_goods])
                            filt_car = {}
                            buy_money = 0
                            nbuy_car = []
                        else:
                            print("请正确选择要移除的商品编号")
                            filt_car = {}
                            buy_money = 0
                    else:
                        print("请正确选择要移除的商品编号")
                        filt_car = {}
                        buy_money = 0
        elif choise_id.upper() == "Q":
            if len(record_car):
                flag = 0
                last_car = {}
                for u in record_car:
                    filt_car.setdefault(u, record_car.count(u))
                print("您本次成功购买了如下商品：")
                for s in filt_car:
                    print(s[0] + " 总共" + str(filt_car[s]) + "个" + ",每个单价为" + str(s[1]))
                print("您本次一共消费%s元，还剩余额%s元" % (buy_money, recharge))
            else:
                print("您没有购买任何商品，你的余额为%s" % recharge)
                flag = 0
        else:
            print("输入错误，请重新选择商品编号")
else:
    print("金额输入有误，请重新开始程序")
