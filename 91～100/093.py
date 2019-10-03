#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @IDE     : PyCharm


if __name__ == '__main__':
    import time
    start = time.process_time()
    for i in range(10000):
        print(i)
    end = time.process_time()
    print('different is %6.3f' % (end - start))

