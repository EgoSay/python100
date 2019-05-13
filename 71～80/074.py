# @Author  : adairchan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/5/13 12:07
# @IDE     : PyCharm
import random

arr1 = [random.randrange(3, 100, 2) for i in range(4)]
arr2 = [random.randrange(3, 100, 2) for j in range(4)]
print(arr1)
arr1.sort()
print(arr1)

# 连接arr1 和 arr2
print(arr1 + arr2)
arr1.extend(arr2)
print(arr1)
