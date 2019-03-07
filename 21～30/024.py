# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/3/4 上午10:23
# @IDE     : PyCharm
from functools import reduce

a = 2.0
b = 1.0
s = 0
for i in range(20):
    s += a / b
    a, b = a, a + b
print(s)

# 方法2
li = list()
li.append(a / b)
for n in range(1, 20):
    b, a = a, a + b
    li.append(a / b)
print(reduce(lambda x, y: x + y, li))
