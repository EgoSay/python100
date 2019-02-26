# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/2/26 下午4:46
# @IDE     : PyCharm


def add(x, y):
    x_sum = x
    flag = x
    for i in range(y - 1):
        x = x * 10 + flag
        x_sum += x
    return x_sum


if __name__ == '__main__':
    a = int(input('请输入a:'))
    n = int(input('要叠加的次数:'))
    print('计算结果为:{}'.format(add(a, n)))
