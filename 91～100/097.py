#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/10/1 下午12:47
# @IDE     : PyCharm

filename = input('输入文件名:\n')
fp = open(filename, "w+")
ch = ''
while '#' not in ch:
    fp.write(ch)
    ch = input('输入字符串:\n')
fp.close()
