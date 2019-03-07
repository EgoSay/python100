# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/3/7 下午12:08
# @IDE     : PyCharm


def factorial_sum(num):
    sum1 = 1
    sum2 = 0
    for i in range(1, num + 1):
        sum1 *= i
        sum2 += sum1
    return sum2


if __name__ == '__main__':
    print(factorial_sum(20))
