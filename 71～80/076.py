# @Author  : adairchan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/5/14 11:15
# @IDE     : PyCharm


def sumfr(n):
    ls = [1 / i for i in range(n, 0, -2)]
    return sum(ls)


if __name__ == '__main__':
    print(sumfr(8))
    print(sumfr(11))