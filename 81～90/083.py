#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/7/25 22:06
# @IDE     : PyCharm


def f(n):
    if n == 0:
        return 1
    elif n == 1:
        return 7
    else:
        return f(n-1)*8
num_map = dict()
#算出每位数有多少奇数
for i in range(1,9):
    num_map.setdefault(i, f(i-1)*4)

#输出一共有多少个奇数
for k,v in num_map.items():
    print("\n{0}位数有{1}个奇数".format(k,v))

print("\n0—7所能组成的奇数个数总计有{0}".format(sum(num_map.values())))