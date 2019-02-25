# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/2/25 下午4:14
# @IDE     : PyCharm


def reduce_num(n):
    if not isinstance(n, int) or n <= 0:
        print('请输入一个正确的数字 !')
        exit(0)
    elif num in [1]:
        print('{}'.format(n))
    print('{} = '.format(n), end="")
    while n != 1:
        for i in range(2, int(num / 2)):
            if n % i == 0:
                n = int(n / i)
                if n == 1:
                    print(i, end=" ")
                else:
                    print('{} *'.format(i), end="")
                break


if __name__ == '__main__':
    num = int(input('输入一个整数:'))
    reduce_num(num)
