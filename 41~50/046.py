# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/3/21 上午10:04
# @IDE     :PyCharm


def power(x):
    if x ** 2 >= 50:
        print('{}的平方为:{},不小于50，继续'.format(x, x ** 2))
    else:
        print('{}的平方为:{},小于50，退出'.format(x, x ** 2))
        quit()


while True:
    x = int(input())
    power(x)
