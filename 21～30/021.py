# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/2/27 下午4:06
# @IDE     : PyCharm

last = 1
for i in range(9):
    num = (last + 1) * 2
    last = num

print("第一天摘了:{}".format(num))


# 改进版
def peach(n):
    return 1 if n == 1 else (peach(n - 1) + 1) * 2


for i in range(1, 11):
    print('第%d天原有%d个桃子,摘了%d个' % (i, peach(11 - i), peach(11 - i) / 2 + 1))
