# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/2/18 下午6:04
# @IDE     : PyCharm

# time 为第几个月，n 为 3


def rabbit(time, n):
    if time < 1:
        return 0
    elif time == 1:
        return 1
    elif time < n:
        return 1
    else:
        return rabbit(time - 1, n) + rabbit(time - (n - 1), n)


print(rabbit(25, 3))
