#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/7/21 22:58
# @IDE     : PyCharm

for i in range(10, 100):
    if (809 * i >= 1000) and (8 * i <= 100) and (9 * \
        i >= 100) and (809 * i == 800 * i + 9 * i):
        print("这个两位数是: {0}, 809乘以这个两位数{0}的结果是: {1}".format(i, 809 * i))
