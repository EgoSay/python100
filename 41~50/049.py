# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/3/21 上午10:04
# @IDE     : PyCharm

MAXIMUM = lambda x, y: (x > y) * x + (x < y) * y
MINIMUM = lambda x, y: (x > y) * y + (x < y) * x

if __name__ == '__main__':
    a = 10
    b = 20
    print('The larger one is %d' % MAXIMUM(a, b))
    print('The lower one is %d' % MINIMUM(a, b))
