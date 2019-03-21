# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/3/21 上午10:04
# @IDE     : PyCharm

num = 2
def autofunc():
    num = 1
    print('internal block num = %d' % num)
    num += 1
for i in range(3):
    print('the num = %d' % num)
    num += 1
    autofunc()
