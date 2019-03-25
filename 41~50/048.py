# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/3/21 上午10:04
# @IDE     : PyCharm

def compare(i, j):
    if i > j:
        print('%d 大于 %d' % (i,j))
    elif i == j:
        print ('%d 等于 %d' % (i,j))
    elif i < j:
        print ('%d 小于 %d' % (i,j))
    else:
        print('未知')


if __name__ == '__main__':
    n1 = int(input())
    n2 = int(input())
    compare(n1, n2)
