#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @IDE     : PyCharm


def encode(num):
    s = str(num)
    n = ""
    for i in range(len(s)):
        n += str((int(s[i]) + 5) % 10)
    return int(n[::-1])


print(encode(1234))
