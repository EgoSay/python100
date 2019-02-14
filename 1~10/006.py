# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/2/14 下午3:42
# @IDE     : PyCharm

import sys


# 方法1
def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        print(a, end=" ")


# 方法2
def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if counter >= n:
            return
        a, b = b, a + b
        counter += 1
        yield a  # yield 的作用就是把一个函数变成一个 generator(生成器)


if __name__ == '__main__':
    fib(10)
    print()
    f = fibonacci(10)
    while True:
        try:
            print(next(f), end=" ")
        except StopIteration:
            sys.exit()
