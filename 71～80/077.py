# @Author  : adairchan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/5/14 11:07
# @IDE     : PyCharm
import random

list1 = [random.randrange(3, 100, 2) for i in range(10)]
print(list1)
for li in list1:
    print(li)