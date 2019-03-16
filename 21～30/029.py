# @Author  : codeAC
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/3/16 23:17
# @IDE     : PyCharm
"""
给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字
"""
from math import floor


def func(n, figures, li):
    # n < 10是一个个位数
    if floor(n / 10) == 0 and n % 10 != 0:
        li.append(floor(n))
    # n > 10
    elif n / 10 >= 1:
        figures += 1
        li.append(floor(n % 10))
        func(n / 10, figures, li)
    return li


if __name__ == '__main__':
    num = int(input())
    lists = list()
    size = len(func(num, 1, lists))
    print("这是一个{0}位数".format(size))
    for i in range(size):
        print(lists[i])
