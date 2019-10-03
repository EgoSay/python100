#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @IDE     : PyCharm


def test():
    for i in range(30):
        print(i)


if __name__ == '__main__':
    from timeit import timeit
    t = timeit('test()', 'from __main__ import test', number=1)
    print(t)

