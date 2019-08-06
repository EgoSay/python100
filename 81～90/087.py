#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/8/6 上午9:41
# @IDE     : PyCharm

if __name__ == '__main__':
    class Student:
        x = 0
        c = 0

    def f(stu):
        stu.x = 20
        stu.c = 'c'


    a = Student()
    a.x = 3
    a.c = 'a'
    f(a)
    print(a.x, a.c)
