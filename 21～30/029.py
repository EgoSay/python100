# @Author  : codeAC
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/3/16 23:17
# @IDE     : PyCharm
"""
给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字
"""
from math import floor


def func(num, figures):
    if num / 10 == 0 and num % 10 != 0:
        print(floor(num % 10))
    elif num / 10 >= 1:
        figures += 1
        print(floor(num % 10))
        func(num / 10, figures)
    return figures


if __name__ == '__main__':
    num = int(input())
    print("这是一个{0}位数".format(func(num, 1)))