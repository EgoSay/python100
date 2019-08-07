#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/8/7 上午10:11
# @IDE     : PyCharm
import random

for i in range(1, 7):
    a = random.randint(0, 50)
    print(a, '\n')
    for j in range(0, a):
        print('*', end='')
    print('\n')
