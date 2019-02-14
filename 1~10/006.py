# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/2/14 下午3:42
# @IDE     : PyCharm


def fib(n):
    a, b = 0, 1
    for i in range(n - 1):
        a, b = b, a + b
        print(a)


# 输出了第10个斐波那契数列
fib(10)
