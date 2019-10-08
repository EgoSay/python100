#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/10/8 8:27 下午
# @IDE     : PyCharm

if __name__ == '__main__':
    import string

    fp = open('test1.txt')
    a = fp.read()
    fp.close()

    fp = open('test2.txt')
    b = fp.read()
    fp.close()

    fp = open('test3.txt', 'w')
    l = list(a + b)
    l.sort()
    s = ''
    s = s.join(l)
    fp.write(s)
    fp.close()