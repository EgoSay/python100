# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/2/21 下午8:52
# @IDE     : PyCharm
from math import sqrt

for i in range(101, 201):
    flag = int(sqrt(i + 1))
    for j in range(2, flag):
        if i % j == 0:
            break

    else:
        print(i)
