#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/7/22 14:39
# @IDE     : PyCharm

# 其他进制
oct_num = input("输入一个8进制的数：")
dec_num = int(oct_num, 8)
print("转换成十进制为：{}".format(dec_num))