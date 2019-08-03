#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/8/3 21:17
# @IDE     : PyCharm
if __name__ == "__main__":
    i = int(input('input a number:'))
    sum = 9
    while sum % i != 0:
        sum = sum * 10 + 9

    print(sum)